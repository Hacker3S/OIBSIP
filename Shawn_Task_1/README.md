# 🎙️ Project 1 — Voice Assistant
**Intern:** Shawn Sreeju Sampath | **ID:** OIB/A2/IP5642
**Organization:** Oasis Infobyte | **Domain:** Python Programming

---

## 📌 Project Overview

A Python-based Voice Assistant that listens to voice commands through the microphone, understands them, and responds through text-to-speech. This project simulates a real-world AI assistant experience using only Python libraries — no cloud AI required.

---

## 🎯 Problem Statement

Users often need to perform repetitive tasks (checking time, searching the web, greeting) manually by typing. This project automates these interactions using voice, making computing more accessible and hands-free.

---

## 💡 Creativity & Problem-Solving Approach

The assistant is designed with a command-matching pipeline:

```
Microphone Input → Speech-to-Text → Keyword Detection → Action Execution → Text-to-Speech Response
```

Instead of a rigid command list, the assistant uses keyword detection inside the recognized text — making it flexible to natural phrasing like "what's the time" or "tell me the time" — both work.

---

## 🛠️ Tools & Technologies Used

| Tool / Library | Version | Purpose |
|---|---|---|
| Python | 3.x | Core programming language |
| `SpeechRecognition` | 3.10+ | Converts microphone audio to text |
| `pyttsx3` | 2.90 | Text-to-speech engine (offline) |
| `PyAudio` | 0.2.14 | Microphone audio capture |
| `datetime` | Built-in | Fetches current time and date |
| `webbrowser` | Built-in | Opens Google search in browser |
| `os` | Built-in | System-level operations |

---

## 📁 Project Structure

```
Shawn_Task_1/
│
├── voice_assistant.py      ← Main script
├── requirements.txt        ← All dependencies
└── README.md               ← This file
```

---

## ⚙️ Installation & Setup

### Step 1 — Install Python
Download Python 3.x from [python.org](https://python.org) and ensure it is added to PATH.

### Step 2 — Install Dependencies
Open terminal in the project folder and run:
```bash
pip install SpeechRecognition pyttsx3 pyaudio
```
> ⚠️ On Windows, if PyAudio fails: download the `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install with `pip install filename.whl`

### Step 3 — Run the Project
```bash
python voice_assistant.py
```

---

## 🧠 How It Works — Step by Step

**Step 1:** The program initializes the text-to-speech engine (`pyttsx3`) and microphone listener (`speech_recognition`).

**Step 2:** It greets the user with "Hello! I am your Python Voice Assistant. How can I help you?"

**Step 3:** The `listen()` function activates the microphone, adjusts for ambient noise, and records audio.

**Step 4:** The recorded audio is sent to Google's Speech Recognition API to convert it to text.

**Step 5:** The `process_command()` function checks for keywords:
- If "hello" → responds with a greeting
- If "time" → fetches and speaks current time using `datetime`
- If "date" → speaks today's date
- If "search" → extracts query and opens Google in the browser
- If "exit" or "quit" → closes the program gracefully

**Step 6:** The response is spoken back using `pyttsx3`.

**Step 7:** The loop continues until the user says "exit".

---

## ✅ Features Implemented

- Greets the user on startup
- Responds to "Hello"
- Tells current time on command
- Tells today's date on command
- Performs Google web search from voice query
- Handles unrecognized commands without crashing
- Clean exit on "exit" or "quit" command
- Ambient noise adjustment for better recognition accuracy

---

## 📋 Sample Interaction

```
Assistant: Hello! I am your Python Voice Assistant. How can I help you?
User: [says] "Hello"
Assistant: "Hello! How are you doing today?"

User: [says] "What is the time?"
Assistant: "The current time is 3:45 PM"

User: [says] "Search Python tutorials"
Assistant: "Searching for Python tutorials..."
[Browser opens: https://www.google.com/search?q=Python+tutorials]

User: [says] "Exit"
Assistant: "Goodbye! Have a great day!"
[Program ends]
```

---

## 📦 requirements.txt

```
SpeechRecognition==3.10.0
pyttsx3==2.90
pyaudio==0.2.14
```

---

## 🧩 Challenges & Solutions

| Challenge | Solution |
|---|---|
| PyAudio installation fails on Windows | Used pre-built `.whl` file from unofficial binaries |
| Background noise causes wrong recognition | Used `adjust_for_ambient_noise()` before listening |
| No internet — Google API fails | Added `try/except` with fallback message |
| Multiple words in search query | Used string splitting and `.join()` to extract full query |

---

## 📈 Learning Outcomes

- Learned real-time audio capture using `PyAudio`
- Understood how Speech Recognition APIs work
- Implemented text-to-speech for natural responses
- Built a looping interactive CLI program with error handling
- Practiced keyword-based NLP logic

---

## 📎 Submission Details

- **File Name:** `Shawn_Task_1`
- **GitHub Repo:** `https://github.com/HACKER3S/OIBSIP/tree/main/Shawn_Task_1`
- **LinkedIn Post:** [Link after posting]
