# 🌤️ Project 4 — Weather App
**Intern:** Shawn Sreeju Sampath | **ID:** OIB/A2/IP5642
**Organization:** Oasis Infobyte | **Domain:** Python Programming

---

## 📌 Project Overview

A graphical Weather Application built using Python, Tkinter, and the OpenWeatherMap API. Users can search for any city worldwide and instantly view real-time weather data including temperature, humidity, wind speed, and weather conditions — all displayed in a clean, user-friendly interface.

---

## 🎯 Problem Statement

Checking the weather requires opening a browser, typing a search, and navigating a cluttered webpage. This project provides a lightweight desktop app that fetches and displays only the essential weather information instantly for any city in the world.

---

## 💡 Creativity & Problem-Solving Approach

The application improves on a basic weather fetcher by:
- **Celsius/Fahrenheit toggle** — user can switch temperature units without re-searching.
- **Secure API key handling** — the key is stored in a `.env` file and loaded with `python-dotenv` instead of being hardcoded, following real-world security best practices.
- **Graceful error handling** — invalid city names, no internet, and API failures each show a specific, helpful message.
- **Dynamic background color** — the app background changes based on weather condition (sunny = warm tones, rainy = cool tones) for visual appeal.

Design flow:
```
User Enters City → API Request Sent → JSON Response Parsed → Data Displayed in GUI → Toggle °C/°F Available
```

---

## 🛠️ Tools & Technologies Used

| Tool / Library | Version | Purpose |
|---|---|---|
| Python | 3.x | Core programming language |
| `tkinter` | Built-in | GUI framework |
| `requests` | 2.31+ | Sending HTTP requests to the weather API |
| `python-dotenv` | 1.0.0 | Loading the API key securely from `.env` |
| `json` | Built-in | Parsing the API response |
| OpenWeatherMap API | Free Tier | Real-time weather data source |
| `os` | Built-in | Reading environment variables |

---

## 📁 Project Structure

```
Shawn_Task_4/
│
├── weather_app.py          ← Main application script
├── .env                    ← Stores API key (NOT pushed to GitHub)
├── .gitignore              ← Excludes .env from version control
├── requirements.txt        ← Dependencies
└── README.md               ← This file
```

> ⚠️ **Important:** The `.env` file contains your private API key. It is listed in `.gitignore` and must NEVER be pushed to GitHub.

---

## 🔑 API Key Setup

### Step 1 — Get a Free API Key
1. Go to [openweathermap.org](https://openweathermap.org/)
2. Click Sign Up → Create a free account
3. Go to **API Keys** section in your profile
4. Copy your default API key

### Step 2 — Create the `.env` File
In the project folder, create a file named `.env` and add:
```
API_KEY=your_api_key_here
```

### Step 3 — Create `.gitignore`
Create a `.gitignore` file with:
```
.env
```

---

## ⚙️ Installation & Setup

### Step 1 — Install Dependencies
```bash
pip install requests python-dotenv
```

### Step 2 — Add API Key
Follow the API Key Setup steps above.

### Step 3 — Run the Project
```bash
python weather_app.py
```

---

## 🧠 How It Works — Step by Step

**Step 1:** The `.env` file is read using `python-dotenv` to load the API key securely into an environment variable.

**Step 2:** The Tkinter window opens with a search bar and a "Get Weather" button.

**Step 3:** The user types a city name and clicks the button. The `fetch_weather()` function is called.

**Step 4:** An HTTP GET request is sent to the OpenWeatherMap API:
```
https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric
```

**Step 5:** The JSON response is parsed to extract:
- `main.temp` → Temperature
- `main.humidity` → Humidity percentage
- `wind.speed` → Wind speed in m/s
- `weather[0].description` → Weather condition text
- `weather[0].main` → Weather category (used for background color logic)

**Step 6:** All extracted values are displayed in the GUI using Tkinter labels, updated dynamically.

**Step 7:** If the user clicks the °C/°F toggle, the temperature is converted locally (no new API call needed):
```python
fahrenheit = (celsius * 9/5) + 32
```

**Step 8:** Error handling covers:
- City not found (API returns 404) → "City not found. Please check the spelling."
- No internet connection → "Network error. Please check your internet connection."
- Empty search field → "Please enter a city name."

---

## ✅ Features Implemented

- Real-time weather data from OpenWeatherMap API
- Search by city name (worldwide)
- Displays: Temperature, Humidity, Wind Speed, Weather Condition
- Celsius to Fahrenheit toggle
- Secure API key management with `.env` and `python-dotenv`
- Descriptive error messages for all failure scenarios
- Dynamic UI response on button click
- Clean Tkinter GUI layout

---

## 📋 Sample Output

```
City: Mumbai

🌡 Temperature: 32°C
💧 Humidity: 78%
💨 Wind Speed: 5.2 m/s
🌤 Condition: Partly Cloudy
```

```
City: xyzabc123

❌ City not found. Please check the spelling.
```

---

## 📦 requirements.txt

```
requests==2.31.0
python-dotenv==1.0.0
```

---

## 🧩 Challenges & Solutions

| Challenge | Solution |
|---|---|
| Hardcoding API key is a security risk | Used `python-dotenv` to load key from `.env` file |
| API key not active immediately after signup | OpenWeatherMap keys activate within 10–30 minutes of creation |
| App crashes on no internet | Wrapped API call in `try/except requests.exceptions.ConnectionError` |
| JSON keys throw errors for some cities | Used `.get()` with fallback values: `data.get('main', {}).get('temp', 'N/A')` |

---

## 📈 Learning Outcomes

- Understood REST API integration using the `requests` library
- Practiced JSON parsing and data extraction
- Learned secure credential management using environment variables
- Built a fully dynamic Tkinter GUI that updates based on API data
- Implemented comprehensive error handling for network applications

---

## 📎 Submission Details

- **File Name:** `Shawn_Task_4`
- **GitHub Repo:** `https://github.com/HACKER3S/OIBSIP/tree/main/Shawn_Task_4`
- **LinkedIn Post:** [Link after posting]
