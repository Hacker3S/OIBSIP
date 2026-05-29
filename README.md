# 🐍 OIBSIP — Python Programming Internship
### Oasis Infobyte | AICTE Approved Internship Program

---

<p align="center">
  <img src="https://img.shields.io/badge/Intern-Shawn%20Sreeju%20Sampath-gold?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Domain-Python%20Programming-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Organization-Oasis%20Infobyte-darkblue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-In%20Progress-orange?style=for-the-badge" />
</p>

---

## 👤 Intern Details

| Field | Details |
|-------|---------|
| **Name** | Shawn Sreeju Sampath |
| **Program** | AICTE Oasis Infobyte Python Programming Internship |
| **Start Date** | June 5, 2026 |
| **Deadline** | July 15, 2026 |
| **Domain** | Python Programming |
| **Minimum Required** | 3 out of 5 Projects |

---

## 📁 Project Overview

| # | Project | Description | Tech Stack | Status | Demo |
|---|---------|-------------|------------|--------|------|
| 1 | [Voice Assistant](#project-1--voice-assistant) | A voice-controlled assistant that responds to commands, tells time/date, and searches the web | Python, SpeechRecognition, pyttsx3 | ⏳ Pending | — |
| 2 | [BMI Calculator](#project-2--bmi-calculator) | GUI-based BMI calculator with health categorization, data storage and trend visualization | Python, Tkinter, Matplotlib | ⏳ Pending | — |
| 3 | [Random Password Generator](#project-3--random-password-generator) | Generates strong passwords with GUI, complexity options and clipboard copy support | Python, Tkinter, pyperclip | ⏳ Pending | — |
| 4 | [Weather App](#project-4--weather-app) | Fetches real-time weather data from an API and displays temperature, humidity, conditions | Python, Tkinter, OpenWeatherMap API | ⏳ Pending | — |
| 5 | [Chat Application](#project-5--chat-application) | Real-time client-server chat application using socket programming | Python, socket, threading | ⏳ Pending | — |

> ✅ Update the Status column as you complete each project. Change ⏳ Pending → 🔄 In Progress → ✅ Completed

---

## 🗂️ Repository Structure

```
OIBSIP/
│
├── README.md
│
├── Shawn_Task_1/
│   ├── voice_assistant.py
│   └── README.md
│
├── Shawn_Task_2/
│   ├── bmi_calculator.py
│   └── README.md
│
├── Shawn_Task_3/
│   ├── password_generator.py
│   └── README.md
│
├── Shawn_Task_4/
│   ├── weather_app.py
│   ├── .env              ← (API key stored here, NOT pushed to GitHub)
│   └── README.md
│
└── Shawn_Task_5/
    ├── server.py
    ├── client.py
    └── README.md
```

---

## Project 1 — Voice Assistant

**Folder:** `Shawn_Task_1/`

### Description
A Python-based voice assistant that listens to voice commands and responds. It can greet the user, tell the current time and date, and search Google based on queries.

### Features
- Responds to "Hello" with a greeting
- Tells current time and date on request
- Opens Google search based on voice query
- Text-to-speech output using `pyttsx3`
- Handles unrecognized commands gracefully

### Tech Stack
- Python 3.x
- `SpeechRecognition` — for capturing voice input
- `pyttsx3` — for text-to-speech output
- `datetime` — for time/date
- `webbrowser` — for web search

### How to Run
```bash
cd Shawn_Task_1
pip install SpeechRecognition pyttsx3 pyaudio
python voice_assistant.py
```

---

## Project 2 — BMI Calculator

**Folder:** `Shawn_Task_2/`

### Description
A GUI-based Body Mass Index (BMI) calculator built with Tkinter. Users can enter weight and height, calculate their BMI, view their health category, and track BMI history with a trend graph.

### Features
- Clean Tkinter GUI interface
- BMI calculation using standard formula
- Health category classification (Underweight / Normal / Overweight / Obese)
- Saves BMI history to a local file
- Displays historical BMI trend using Matplotlib

### Tech Stack
- Python 3.x
- `tkinter` — GUI (built-in)
- `matplotlib` — data visualization
- `json` — data storage

### How to Run
```bash
cd Shawn_Task_2
pip install matplotlib
python bmi_calculator.py
```

---

## Project 3 — Random Password Generator

**Folder:** `Shawn_Task_3/`

### Description
A GUI application that generates strong, random passwords based on user-defined criteria including length, and inclusion of uppercase letters, numbers, and special symbols.

### Features
- Tkinter GUI with intuitive controls
- Customizable password length (slider)
- Toggle options: uppercase, lowercase, numbers, symbols
- Password strength indicator
- One-click clipboard copy
- Generate multiple passwords at once

### Tech Stack
- Python 3.x
- `tkinter` — GUI (built-in)
- `random` / `string` / `secrets` — password generation
- `pyperclip` — clipboard support

### How to Run
```bash
cd Shawn_Task_3
pip install pyperclip
python password_generator.py
```

---

## Project 4 — Weather App

**Folder:** `Shawn_Task_4/`

### Description
A weather application that fetches real-time weather data from the OpenWeatherMap API and displays it in a clean GUI. Users can search any city to get temperature, humidity, wind speed and weather description.

### Features
- City-based weather search
- Displays temperature (°C), humidity, wind speed, weather condition
- Weather icons based on conditions
- Error handling for invalid city names or API failures
- Supports Celsius/Fahrenheit toggle

### Tech Stack
- Python 3.x
- `tkinter` — GUI (built-in)
- `requests` — API calls
- `python-dotenv` — secure API key handling
- OpenWeatherMap API (free tier)

### How to Run
```bash
cd Shawn_Task_4
pip install requests python-dotenv
# Add your API key in a .env file: API_KEY=your_key_here
python weather_app.py
```

> Get your free API key at: https://openweathermap.org/api

---

## Project 5 — Chat Application

**Folder:** `Shawn_Task_5/`

### Description
A real-time chat application built using Python's socket and threading modules. Implements a client-server architecture where multiple clients can connect to a server and exchange messages.

### Features
- Server handles multiple clients simultaneously using threading
- Clients can choose a username
- Real-time message broadcasting to all connected users
- Displays join/leave notifications
- Graceful disconnection handling

### Tech Stack
- Python 3.x
- `socket` — network communication (built-in)
- `threading` — multi-client handling (built-in)

### How to Run
```bash
cd Shawn_Task_5

# Terminal 1 — Start the server
python server.py

# Terminal 2 — Start a client
python client.py

# Terminal 3 — Start another client
python client.py
```

---

## 📋 Submission Checklist

- [ ] GitHub repo named exactly `OIBSIP`
- [ ] Each project in its own folder with a README
- [ ] At least **3 projects** completed and pushed
- [ ] Video demo recorded for each project
- [ ] Video shared on LinkedIn with hashtags: `#oasisinfobyte #oasisinfobytefamily #internship #python`
- [ ] Submitted via the official batch submission form
- [ ] File naming format followed: `Shawn_Task1`, `Shawn_Task2`, etc.

---

## 📅 Recommended Timeline

| Dates | Goal |
|-------|------|
| June 5–8 | Setup repo, Python environment, understand all tasks |
| June 9–16 | Build & push Task 1 (Voice Assistant) |
| June 17–22 | Build & push Task 2 (BMI Calculator) |
| June 23–28 | Build & push Task 3 (Password Generator) |
| June 29 – July 5 | Build & push Task 4 (Weather App) |
| July 6–12 | Build & push Task 5 (Chat App) |
| July 13–15 | Final review, submit all tasks via form |

---

## 🔗 Important Links

- 🌐 Oasis Infobyte: [oasisinfobyte.com](https://oasisinfobyte.com)
- 💬 Telegram Community: [t.me/oasisinfobyte](https://t.me/oasisinfobyte)
- 📋 Submission Form: *(Use link from your offer letter)*

---

## 📜 Certificate

> Certificates are issued only after successful evaluation of all submitted projects. Ensure submissions are complete, original, well-documented, and include a video demonstration.

---

<p align="center">Made with ❤️ by <strong>Shawn Sreeju Sampath</strong> | Oasis Infobyte Python Internship 2026</p>
