# ─────────────────────────────────────────────────────────
# Chat Application — CLIENT (GUI)
# Oasis Infobyte Internship (Task 5)
# Intern : Shawn Sreeju Sampath | ID: OIB/A2/IP5642
# ─────────────────────────────────────────────────────────
# Run this file AFTER server.py is already running.
# Open multiple times to simulate multiple users.
# ─────────────────────────────────────────────────────────

import tkinter as tk
from tkinter import messagebox
import socket
import threading

# ── Server Configuration (must match server.py) ───────────
HOST = "127.0.0.1"
PORT = 55555


# ── Main Application Class ────────────────────────────────
class ChatClient:
    def __init__(self, root):
        self.root     = root
        self.root.title("Chat App — OIBSIP | Shawn Sreeju Sampath")
        self.root.geometry("500x620")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.client   = None
        self.username = None

        self.show_login()

    # ── Login Screen ───────────────────────────────────────
    def show_login(self):
        self.login_frame = tk.Frame(self.root, bg="#1a1a2e")
        self.login_frame.pack(expand=True)

        tk.Label(self.login_frame,
                 text="💬  Chat Application",
                 font=("Arial", 24, "bold"),
                 bg="#1a1a2e", fg="#f0c040").pack(pady=(0, 4))

        tk.Label(self.login_frame,
                 text="Oasis Infobyte Internship  |  Shawn Sreeju Sampath",
                 font=("Arial", 9), bg="#1a1a2e", fg="#777777").pack()

        tk.Label(self.login_frame,
                 text="Built with Python  •  socket  •  threading  •  tkinter",
                 font=("Arial", 8), bg="#1a1a2e", fg="#444444").pack(pady=(2, 30))

        tk.Label(self.login_frame,
                 text="Enter your username:",
                 font=("Arial", 12), bg="#1a1a2e", fg="white").pack(pady=5)

        self.username_entry = tk.Entry(
            self.login_frame,
            font=("Arial", 13), width=20,
            bg="#16213e", fg="white",
            insertbackground="white",
            relief="flat", bd=8, justify="center")
        self.username_entry.pack(pady=5, ipady=7)
        self.username_entry.bind("<Return>", lambda e: self.connect())
        self.username_entry.focus()

        tk.Button(self.login_frame,
                  text="Join Chat  ➤",
                  font=("Arial", 12, "bold"),
                  bg="#f0c040", fg="#1a1a2e",
                  padx=22, pady=9,
                  cursor="hand2", relief="flat",
                  command=self.connect).pack(pady=16)

        self.login_status = tk.Label(
            self.login_frame, text="",
            font=("Arial", 10), bg="#1a1a2e",
            fg="#e74c3c", wraplength=340, justify="center")
        self.login_status.pack()

    # ── Connect to Server ──────────────────────────────────
    def connect(self):
        username = self.username_entry.get().strip()

        if not username:
            self.login_status.config(text="⚠  Please enter a username.")
            return
        if len(username) > 16:
            self.login_status.config(
                text="⚠  Username must be 16 characters or less.")
            return

        self.username = username
        self.login_status.config(
            text="Connecting to server...", fg="#f0c040")
        self.root.update()

        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((HOST, PORT))

            # Server sends "USERNAME" prompt — respond with our username
            prompt = self.client.recv(1024).decode("utf-8")
            if prompt == "USERNAME":
                self.client.send(username.encode("utf-8"))

            # Move to chat screen
            self.login_frame.destroy()
            self.show_chat()

            # Background thread to receive messages
            recv_thread = threading.Thread(
                target=self.receive_messages, daemon=True)
            recv_thread.start()

        except ConnectionRefusedError:
            self.login_status.config(
                text="❌  Cannot connect to server.\n"
                     "Make sure server.py is running first!",
                fg="#e74c3c")
        except Exception as e:
            self.login_status.config(
                text=f"❌  Error: {e}", fg="#e74c3c")

    # ── Chat Screen ────────────────────────────────────────
    def show_chat(self):
        self.root.title(f"Chat App — {self.username}  |  OIBSIP")

        # ── Header ─────────────────────────────────────────
        header = tk.Frame(self.root, bg="#16213e", pady=12)
        header.pack(fill="x")

        tk.Label(header,
                 text="💬  Live Chat Room",
                 font=("Arial", 16, "bold"),
                 bg="#16213e", fg="#f0c040").pack()

        tk.Label(header,
                 text=f"Logged in as:  {self.username}",
                 font=("Arial", 9), bg="#16213e",
                 fg="#2ecc71").pack()

        # ── Chat Display ───────────────────────────────────
        chat_outer = tk.Frame(self.root, bg="#1a1a2e")
        chat_outer.pack(fill="both", expand=True, padx=15, pady=(10, 5))

        self.chat_display = tk.Text(
            chat_outer,
            font=("Arial", 11),
            bg="#0f3460", fg="white",
            relief="flat", bd=0,
            state="disabled",
            wrap="word",
            padx=12, pady=10)
        self.chat_display.pack(fill="both", expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(self.chat_display)
        self.chat_display.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.chat_display.yview)

        # Text colour tags
        self.chat_display.tag_config(
            "server",  foreground="#f0c040", font=("Arial", 10, "italic"))
        self.chat_display.tag_config(
            "self",    foreground="#2ecc71", font=("Arial", 11, "bold"))
        self.chat_display.tag_config(
            "other",   foreground="#3498db", font=("Arial", 11, "bold"))
        self.chat_display.tag_config(
            "body",    foreground="white",   font=("Arial", 11))

        # ── Input Area ─────────────────────────────────────
        input_frame = tk.Frame(self.root, bg="#16213e", pady=10, padx=15)
        input_frame.pack(fill="x")

        self.message_entry = tk.Entry(
            input_frame,
            font=("Arial", 12), width=30,
            bg="#0f3460", fg="white",
            insertbackground="white",
            relief="flat", bd=6)
        self.message_entry.pack(
            side="left", fill="x", expand=True, ipady=7)
        self.message_entry.bind("<Return>", lambda e: self.send_message())
        self.message_entry.focus()

        tk.Button(input_frame,
                  text="Send  ➤",
                  font=("Arial", 11, "bold"),
                  bg="#f0c040", fg="#1a1a2e",
                  padx=14, pady=6,
                  cursor="hand2", relief="flat",
                  command=self.send_message).pack(side="left", padx=(8, 0))

        # ── Disconnect Button ──────────────────────────────
        tk.Button(self.root,
                  text="Disconnect",
                  font=("Arial", 9),
                  bg="#e74c3c", fg="white",
                  padx=10, pady=4,
                  cursor="hand2", relief="flat",
                  command=self.on_close).pack(pady=(0, 8))

    # ── Display a Message in the Chat Box ─────────────────
    def display_message(self, message):
        self.chat_display.config(state="normal")
        self.chat_display.insert(tk.END, "\n")

        if message.startswith("[Server]:"):
            self.chat_display.insert(tk.END, message, "server")

        elif message.startswith(f"[{self.username}]:"):
            # Own message — split name from body
            parts = message.split("]: ", 1)
            self.chat_display.insert(tk.END, parts[0] + "]: ", "self")
            if len(parts) > 1:
                self.chat_display.insert(tk.END, parts[1], "body")

        else:
            # Another user's message
            parts = message.split("]: ", 1)
            self.chat_display.insert(tk.END, parts[0] + "]: ", "other")
            if len(parts) > 1:
                self.chat_display.insert(tk.END, parts[1], "body")

        self.chat_display.config(state="disabled")
        self.chat_display.see(tk.END)          # auto-scroll

    # ── Receive Messages (background thread) ──────────────
    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(2048).decode("utf-8")
                if message:
                    self.root.after(0, self.display_message, message)
                else:
                    break
            except Exception:
                self.root.after(
                    0, self.display_message,
                    "[Server]: Connection lost.")
                break

    # ── Send a Message ─────────────────────────────────────
    def send_message(self):
        message = self.message_entry.get().strip()
        if not message:
            return

        formatted = f"[{self.username}]: {message}"

        try:
            self.client.send(formatted.encode("utf-8"))
            self.display_message(formatted)        # show your own message
            self.message_entry.delete(0, tk.END)
        except Exception:
            messagebox.showerror(
                "Send Failed",
                "Could not send the message.\n"
                "The connection may have been lost.")

    # ── Close Handler ──────────────────────────────────────
    def on_close(self):
        if self.client:
            try:
                self.client.close()
            except Exception:
                pass
        self.root.destroy()


# ── Entry Point ───────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClient(root)
    root.mainloop()
