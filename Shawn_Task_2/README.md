# ⚖️ Project 2 — BMI Calculator
**Intern:** Shawn Sreeju Sampath | **ID:** OIB/A2/IP5642
**Organization:** Oasis Infobyte | **Domain:** Python Programming

---

## 📌 Project Overview

A graphical Body Mass Index (BMI) Calculator built using Python and Tkinter. The application allows users to input their weight and height, calculates their BMI using the standard WHO formula, classifies it into a health category, stores history locally, and visualizes the trend over time using a graph.

---

## 🎯 Problem Statement

BMI is a universally used health indicator, but most people don't have a quick and accessible tool to track it over time. This project provides a clean desktop GUI application where users can calculate, save, and visualize their BMI history — all in one place.

---

## 💡 Creativity & Problem-Solving Approach

The application goes beyond a simple calculator by adding:
- **Color-coded results** — each BMI category has a unique color (green = normal, blue = underweight, orange = overweight, red = obese) for instant visual feedback.
- **Persistent history** — BMI records are saved to a local JSON file so data is retained between sessions.
- **Trend graph** — A Matplotlib chart shows how BMI has changed over time, making it a health tracking tool, not just a calculator.

Design flow:
```
User Inputs Weight & Height → BMI Calculated → Category Shown → Data Saved → History Viewable as Graph
```

---

## 🛠️ Tools & Technologies Used

| Tool / Library | Version | Purpose |
|---|---|---|
| Python | 3.x | Core programming language |
| `tkinter` | Built-in | GUI framework for the desktop app |
| `matplotlib` | 3.7+ | Plotting the BMI history graph |
| `json` | Built-in | Storing and reading BMI history data |
| `datetime` | Built-in | Timestamping each BMI record |
| `messagebox` (tkinter) | Built-in | Popup alerts for errors and confirmations |

---

## 📁 Project Structure

```
Shawn_Task_2/
│
├── bmi_calculator.py       ← Main application script
├── bmi_history.json        ← Auto-created: stores BMI records
├── requirements.txt        ← Dependencies
└── README.md               ← This file
```

---

## ⚙️ Installation & Setup

### Step 1 — Install Python
Ensure Python 3.x is installed with `tkinter` (included by default in standard Python installations).

### Step 2 — Install Dependencies
```bash
pip install matplotlib
```

### Step 3 — Run the Project
```bash
python bmi_calculator.py
```

---

## 🧠 How It Works — Step by Step

**Step 1:** The Tkinter window launches with two input fields — Weight (kg) and Height (m) — and a Calculate button.

**Step 2:** On clicking Calculate, both inputs are validated:
- Checked for empty fields
- Checked for non-numeric input
- Checked for unrealistic values (e.g., height = 0)

**Step 3:** BMI is calculated using the WHO formula:
```
BMI = Weight (kg) / Height (m)²
```

**Step 4:** The result is classified:

| BMI Range | Category | Color |
|---|---|---|
| Below 18.5 | Underweight | 🔵 Blue |
| 18.5 – 24.9 | Normal Weight | 🟢 Green |
| 25.0 – 29.9 | Overweight | 🟠 Orange |
| 30.0 and above | Obese | 🔴 Red |

**Step 5:** The BMI value, category, and timestamp are saved to `bmi_history.json`.

**Step 6:** Clicking "View History" reads the JSON file and opens a Matplotlib line graph showing all recorded BMI values over time with horizontal reference lines marking category boundaries.

---

## ✅ Features Implemented

- Clean Tkinter GUI with labels, entry fields, and buttons
- Accurate BMI calculation using the WHO standard formula
- Color-coded health category display
- Input validation with descriptive error messages
- Persistent data storage using JSON
- BMI history graph with Matplotlib
- Clear/Reset button to start a new entry
- Reference lines on graph for WHO category boundaries

---

## 📋 Sample Input & Output

```
Input:
  Weight: 70 kg
  Height: 1.75 m

Output:
  BMI: 22.86
  Category: Normal Weight ✅ (shown in green)
  Saved to history!
```

```
Input:
  Weight: 100 kg
  Height: 1.70 m

Output:
  BMI: 34.60
  Category: Obese ⚠️ (shown in red)
```

---

## 📦 requirements.txt

```
matplotlib==3.7.0
```

---

## 🧩 Challenges & Solutions

| Challenge | Solution |
|---|---|
| Users entering text instead of numbers | Used `try/except ValueError` around `float()` conversion |
| JSON file missing on first run | Used `os.path.exists()` to create it if not present |
| Graph looks cluttered with many data points | Added date formatting on x-axis with `plt.xticks(rotation=45)` |
| Height entered as centimeters by mistake | Added note in UI: "Height must be in meters (e.g., 1.75)" |

---

## 📈 Learning Outcomes

- Built a complete GUI application with Tkinter
- Applied the BMI formula and WHO classification standards
- Implemented data persistence using JSON file storage
- Created data visualizations using Matplotlib
- Practiced input validation and error handling

---

## 📎 Submission Details

- **File Name:** `Shawn_Task_2`
- **GitHub Repo:** `https://github.com/HACKER3S/OIBSIP/tree/main/Shawn_Task_2`
- **LinkedIn Post:** [Link after posting]
