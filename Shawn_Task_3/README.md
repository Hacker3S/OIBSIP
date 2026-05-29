# 🔐 Project 3 — Random Password Generator
**Intern:** Shawn Sreeju Sampath | **ID:** OIB/A2/IP5642
**Organization:** Oasis Infobyte | **Domain:** Python Programming

---

## 📌 Project Overview

A graphical Random Password Generator built with Python and Tkinter. Users can customize password length and character type preferences, generate cryptographically secure passwords, check their strength, and copy them to the clipboard with a single click.

---

## 🎯 Problem Statement

Weak and reused passwords are one of the leading causes of security breaches. Most users don't generate strong passwords because it's inconvenient. This tool makes it fast and effortless to create strong, unique passwords on demand.

---

## 💡 Creativity & Problem-Solving Approach

Unlike basic password generators, this application adds:
- **Password Strength Indicator** — real-time visual bar that rates password strength from Weak to Very Strong based on length and character diversity.
- **`secrets` module instead of `random`** — uses Python's cryptographically secure random generator for true password security.
- **Multiple passwords at once** — users can generate and view several options to choose from.
- **Character exclusion** — users can exclude ambiguous characters like `O`, `0`, `l`, `1` to avoid confusion.

Design flow:
```
User Sets Preferences → Character Pool Built → secrets.choice() Generates Password → Strength Rated → Displayed → One-Click Copy
```

---

## 🛠️ Tools & Technologies Used

| Tool / Library | Version | Purpose |
|---|---|---|
| Python | 3.x | Core programming language |
| `tkinter` | Built-in | GUI framework |
| `secrets` | Built-in | Cryptographically secure password generation |
| `string` | Built-in | Provides character sets (letters, digits, symbols) |
| `pyperclip` | 1.8.2 | Copies password to system clipboard |
| `ttk` (tkinter) | Built-in | Modern styled widgets (Scale slider, Progressbar) |

---

## 📁 Project Structure

```
Shawn_Task_3/
│
├── password_generator.py   ← Main application script
├── requirements.txt        ← Dependencies
└── README.md               ← This file
```

---

## ⚙️ Installation & Setup

### Step 1 — Install Python
Ensure Python 3.x is installed. `tkinter`, `secrets`, and `string` are included by default.

### Step 2 — Install Dependencies
```bash
pip install pyperclip
```

### Step 3 — Run the Project
```bash
python password_generator.py
```

---

## 🧠 How It Works — Step by Step

**Step 1:** The GUI window opens showing a slider (length 8–32), four checkboxes (Uppercase, Lowercase, Numbers, Symbols), and a Generate button.

**Step 2:** The user adjusts the slider and checks desired character types.

**Step 3:** On clicking Generate, the `build_character_pool()` function assembles a pool string from selected character sets:
```python
import string
pool = ""
if uppercase: pool += string.ascii_uppercase   # A-Z
if lowercase: pool += string.ascii_lowercase   # a-z
if numbers:   pool += string.digits            # 0-9
if symbols:   pool += string.punctuation       # !@#$%...
```

**Step 4:** The password is generated using `secrets.choice()` in a loop:
```python
import secrets
password = ''.join(secrets.choice(pool) for _ in range(length))
```
> `secrets` is used instead of `random` because it is designed for security-sensitive applications.

**Step 5:** The `calculate_strength()` function evaluates the password:
- Length < 8 → Weak
- Length 8–11, limited types → Medium
- Length 12+, 3+ types → Strong
- Length 16+, all types → Very Strong

**Step 6:** The strength bar (Progressbar widget) updates its color and fill.

**Step 7:** Clicking "Copy to Clipboard" calls `pyperclip.copy(password)` and shows a confirmation message.

---

## ✅ Features Implemented

- Tkinter GUI with slider, checkboxes, and result display
- Cryptographically secure password generation using `secrets`
- Customizable length (8 to 32 characters)
- Toggle options for uppercase, lowercase, numbers, and symbols
- Real-time password strength indicator (Weak / Medium / Strong / Very Strong)
- One-click clipboard copy using `pyperclip`
- Error shown if no character type is selected
- Generate multiple passwords in sequence

---

## 📋 Sample Output

```
Settings:
  Length: 16
  Uppercase: ✅  Lowercase: ✅  Numbers: ✅  Symbols: ✅

Generated Password: gR7#mKx2@LpQ9!nZ
Strength: ████████████████ Very Strong

[Copy to Clipboard] → ✅ Copied!
```

```
Settings:
  Length: 8
  Uppercase: ✅  Lowercase: ✅  Numbers: ❌  Symbols: ❌

Generated Password: HkrTbAnM
Strength: ████░░░░░░░░░░░░ Medium
```

---

## 📦 requirements.txt

```
pyperclip==1.8.2
```

---

## 🧩 Challenges & Solutions

| Challenge | Solution |
|---|---|
| `random` is not secure enough for passwords | Switched to Python's `secrets` module |
| User selects no character type — empty pool | Added validation: show error if all checkboxes unchecked |
| `pyperclip` not working on Linux | Requires `xclip` or `xsel`: `sudo apt install xclip` |
| Strength calculation was inaccurate | Scored based on both length AND number of character types present |

---

## 📈 Learning Outcomes

- Understood the difference between `random` and `secrets` modules
- Built a fully functional GUI with Tkinter widgets
- Learned character set handling with Python's `string` module
- Implemented clipboard integration using `pyperclip`
- Designed a password strength scoring algorithm

---

## 📎 Submission Details

- **File Name:** `Shawn_Task_3`
- **GitHub Repo:** `https://github.com/HACKER3S/OIBSIP/tree/main/Shawn_Task_3`
- **LinkedIn Post:** [Link after posting]
