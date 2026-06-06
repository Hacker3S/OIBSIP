# ─────────────────────────────────────────────────────────
# Chat Application — SERVER
# Oasis Infobyte Internship (Task 5)
# Intern : Shawn Sreeju Sampath | ID: OIB/A2/IP5642
# ─────────────────────────────────────────────────────────
# Run this file FIRST before launching any client.
# ─────────────────────────────────────────────────────────

import socket
import threading

# ── Server Configuration ──────────────────────────────────
HOST = "127.0.0.1"   # localhost
PORT = 55555

# ── Global State ──────────────────────────────────────────
clients   = []   # list of connected client sockets
usernames = []   # parallel list of usernames


# ── Broadcast ─────────────────────────────────────────────
def broadcast(message, sender_client=None):
    """
    Send a message to all connected clients.
    If sender_client is provided, skip sending to them
    (they display their own message locally).
    """
    for client in clients[:]:          # iterate a copy
        if client != sender_client:
            try:
                client.send(message)
            except Exception:
                remove_client(client)


# ── Remove a Client ───────────────────────────────────────
def remove_client(client):
    """Cleanly remove a disconnected client and notify others."""
    if client in clients:
        index    = clients.index(client)
        username = usernames[index]
        clients.remove(client)
        usernames.remove(username)
        try:
            client.close()
        except Exception:
            pass
        leave_msg = f"[Server]: {username} has left the chat. 👋"
        print(leave_msg)
        broadcast(leave_msg.encode("utf-8"))


# ── Handle One Client ─────────────────────────────────────
def handle_client(client):
    """Continuously receive messages from a client and broadcast them."""
    while True:
        try:
            message = client.recv(2048).decode("utf-8")
            if message:
                print(message)
                broadcast(message.encode("utf-8"), sender_client=client)
            else:
                remove_client(client)
                break
        except Exception:
            remove_client(client)
            break


# ── Accept Connections ────────────────────────────────────
def start_server():
    """Start the server and listen for incoming connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    print("=" * 45)
    print("   Chat Server — OIBSIP | Shawn Sreeju Sampath")
    print("=" * 45)
    print(f"[Server] Running on {HOST}:{PORT}")
    print("[Server] Waiting for clients to connect...")
    print("-" * 45)

    while True:
        client, address = server.accept()
        print(f"[Server] New connection from {address}")

        # Ask the client for their username
        client.send("USERNAME".encode("utf-8"))
        username = client.recv(1024).decode("utf-8").strip()

        usernames.append(username)
        clients.append(client)

        print(f"[Server] '{username}' has joined.")

        # Notify everyone
        broadcast(
            f"[Server]: {username} has joined the chat! 👋".encode("utf-8"))

        # Welcome the new client
        client.send(
            f"[Server]: Welcome, {username}! "
            f"There are {len(clients)} user(s) online.".encode("utf-8"))

        # Spin up a dedicated thread for this client
        thread = threading.Thread(
            target=handle_client, args=(client,), daemon=True)
        thread.start()


# ── Entry Point ───────────────────────────────────────────
if __name__ == "__main__":
    start_server()
