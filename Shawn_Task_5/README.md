# 💬 Project 5 — Chat Application
**Intern:** Shawn Sreeju Sampath | **ID:** OIB/A2/IP5642
**Organization:** Oasis Infobyte | **Domain:** Python Programming

---

## 📌 Project Overview

A real-time terminal-based Chat Application built using Python's built-in `socket` and `threading` modules. It implements a client-server architecture where a central server manages connections and multiple clients can simultaneously send and receive messages in real time.

---

## 🎯 Problem Statement

Understanding how real-time communication works at the network level is a core skill in software development. This project builds a working chat system from scratch — no third-party messaging library — to demonstrate how data flows between computers over a network using sockets.

---

## 💡 Creativity & Problem-Solving Approach

The project uses a **broadcast model**:
- The server acts as a relay hub — it receives messages from one client and immediately sends them to ALL other connected clients.
- **Multi-threading** is used on the server to handle multiple clients simultaneously without blocking.
- Each client gets a dedicated thread on the server, so one slow client doesn't delay others.
- **Username system** — on connect, the client sends its chosen username first, and the server announces join/leave events to the group.

Design flow:
```
Server Starts → Listens for Connections → Client Connects → Sends Username → 
Server Creates Thread for Client → Client Sends Messages → Server Broadcasts to All Others
```

---

## 🛠️ Tools & Technologies Used

| Tool / Library | Version | Purpose |
|---|---|---|
| Python | 3.x | Core programming language |
| `socket` | Built-in | Network communication (TCP/IP) |
| `threading` | Built-in | Handling multiple clients concurrently |
| `sys` | Built-in | Clean program exit handling |

> ✅ This project requires **zero external installations** — everything uses Python's standard library.

---

## 📁 Project Structure

```
Shawn_Task_5/
│
├── server.py               ← Server script (run first)
├── client.py               ← Client script (run per user)
├── README.md               ← This file
└── requirements.txt        ← (No dependencies — all built-in)
```

---

## ⚙️ Installation & Setup

### Step 1 — Install Python
Ensure Python 3.x is installed. No additional packages required.

### Step 2 — Run the Server (Terminal 1)
```bash
python server.py
```
You should see: `Server started on port 55555. Waiting for connections...`

### Step 3 — Run Client 1 (Terminal 2)
```bash
python client.py
```
Enter username when prompted: `Shawn`

### Step 4 — Run Client 2 (Terminal 3)
```bash
python client.py
```
Enter username when prompted: `Alex`

Now both clients can chat in real time!

---

## 🧠 How It Works — Step by Step

### Server Side (`server.py`)

**Step 1:** A TCP socket is created and bound to `localhost` on port `55555`:
```python
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 55555))
server.listen()
```

**Step 2:** The server enters an infinite loop listening for incoming client connections using `server.accept()`.

**Step 3:** When a client connects, it sends its username first. The server stores the username and the connection object in parallel lists.

**Step 4:** A new **thread** is created for each connected client, running the `handle_client()` function, so every client is managed independently and simultaneously.

**Step 5:** The `broadcast()` function loops through all connected clients and sends each message to everyone except the sender.

**Step 6:** If a client disconnects (or an error occurs), the server removes them from the list and broadcasts a "[Username] has left the chat" message to all remaining clients.

### Client Side (`client.py`)

**Step 1:** The client creates a socket and connects to the server:
```python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 55555))
```

**Step 2:** The client starts two threads:
- **Receive thread** — constantly listens for messages from the server and prints them.
- **Send thread** — reads user keyboard input and sends it to the server.

**Step 3:** This two-thread design allows sending and receiving at the same time without either blocking the other.

**Step 4:** Typing "quit" closes the connection gracefully.

---

## ✅ Features Implemented

- TCP socket-based client-server architecture
- Multi-client support using threading (unlimited concurrent users)
- Username system — each user chooses a name on connect
- Real-time message broadcasting to all connected clients
- Join notification: "Shawn has joined the chat!"
- Leave notification: "Shawn has left the chat."
- Graceful disconnection handling (no server crash on client exit)
- Simultaneous send and receive on client using two threads

---

## 📋 Sample Session

```
=== Terminal 1 (Server) ===
Server started on port 55555. Waiting for connections...
[+] Shawn connected.
[+] Alex connected.
[Shawn]: Hello Alex!
[Alex]: Hey Shawn, this is cool!
[-] Alex disconnected.

=== Terminal 2 (Client - Shawn) ===
Enter your username: Shawn
Connected to chat server!
[Server]: Alex has joined the chat.
[Alex]: Hey Shawn, this is cool!
quit
Disconnected.

=== Terminal 3 (Client - Alex) ===
Enter your username: Alex
Connected to chat server!
[Shawn]: Hello Alex!
Hey Shawn, this is cool!
```

---

## 📦 requirements.txt

```
# No external dependencies required.
# Uses only Python built-in modules: socket, threading, sys
```

---

## 🧩 Challenges & Solutions

| Challenge | Solution |
|---|---|
| Server blocks waiting for one client | Used `threading.Thread` to handle each client in parallel |
| Client can't send and receive simultaneously | Ran send and receive in two separate threads on the client |
| Server crashes when a client disconnects abruptly | Wrapped `receive` in `try/except` and removed client from list on error |
| Messages getting mixed up (encoding issues) | Used `.encode('utf-8')` to send and `.decode('utf-8')` to receive all messages |
| Port already in use on restart | Added `server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)` |

---

## 📈 Learning Outcomes

- Understood TCP/IP socket programming from scratch
- Learned how multi-threading enables concurrent connections
- Implemented a real broadcast messaging system
- Handled network errors and graceful disconnection
- Built a working client-server architecture without any framework

---

## 📎 Submission Details

- **File Name:** `Shawn_Task_5`
- **GitHub Repo:** `https://github.com/HACKER3S/OIBSIP/tree/main/Shawn_Task_5`
- **LinkedIn Post:** [Link after posting]
