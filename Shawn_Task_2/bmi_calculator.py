# ─────────────────────────────────────────────────────────
# BMI Calculator — Oasis Infobyte Internship (Task 2)
# Intern : Shawn Sreeju Sampath | ID: OIB/A2/IP5642
# ─────────────────────────────────────────────────────────

import tkinter as tk
from tkinter import messagebox
import json
import os
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ── Constants ─────────────────────────────────────────────
HISTORY_FILE = "bmi_history.json"


# ── Helper Functions ──────────────────────────────────────

def load_history():
    """Load BMI history from JSON file."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []


def save_history(history):
    """Save BMI history to JSON file."""
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def calculate_bmi(weight, height):
    """Calculate BMI using the WHO formula."""
    return round(weight / (height ** 2), 2)


def get_category(bmi):
    """Return category name and display color based on BMI value."""
    if bmi < 18.5:
        return "Underweight", "#3498db"       # Blue
    elif bmi < 25.0:
        return "Normal Weight", "#2ecc71"     # Green
    elif bmi < 30.0:
        return "Overweight", "#f39c12"        # Orange
    else:
        return "Obese", "#e74c3c"             # Red


def get_advice(category):
    """Return a health tip based on BMI category."""
    tips = {
        "Underweight"   : "Consider a balanced, calorie-rich diet and consult a nutritionist.",
        "Normal Weight" : "Great job! Keep up your healthy lifestyle and regular exercise.",
        "Overweight"    : "Try regular physical activity and a balanced, low-calorie diet.",
        "Obese"         : "Please consult a healthcare provider for a personalised health plan.",
    }
    return tips.get(category, "")


# ── Main Application Class ────────────────────────────────

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator — OIBSIP | Shawn Sreeju Sampath")
        self.root.geometry("500x620")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        self.history = load_history()
        self.build_ui()

    # ── UI Builder ─────────────────────────────────────────
    def build_ui(self):

        # Title section
        tk.Label(self.root, text="⚖  BMI Calculator",
                 font=("Arial", 22, "bold"),
                 bg="#1a1a2e", fg="#f0c040").pack(pady=(20, 2))

        tk.Label(self.root,
                 text="Oasis Infobyte Internship  |  Shawn Sreeju Sampath",
                 font=("Arial", 9), bg="#1a1a2e", fg="#777777").pack()

        # ── Input Frame ────────────────────────────────────
        input_frame = tk.Frame(self.root, bg="#16213e", padx=25, pady=20)
        input_frame.pack(pady=20, padx=30, fill="x")

        # Weight
        tk.Label(input_frame, text="Weight (kg):",
                 font=("Arial", 12), bg="#16213e", fg="white").grid(
                 row=0, column=0, sticky="w", pady=10)

        self.weight_entry = tk.Entry(
            input_frame, font=("Arial", 12), width=14,
            bg="#0f3460", fg="white", insertbackground="white",
            relief="flat", bd=5)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=10)

        # Height
        tk.Label(input_frame, text="Height (m):",
                 font=("Arial", 12), bg="#16213e", fg="white").grid(
                 row=1, column=0, sticky="w", pady=10)

        self.height_entry = tk.Entry(
            input_frame, font=("Arial", 12), width=14,
            bg="#0f3460", fg="white", insertbackground="white",
            relief="flat", bd=5)
        self.height_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(input_frame, text="Enter in metres  e.g. 1.75",
                 font=("Arial", 8), bg="#16213e", fg="#666666").grid(
                 row=2, column=1, sticky="w", padx=10)

        # ── Buttons ────────────────────────────────────────
        btn_frame = tk.Frame(self.root, bg="#1a1a2e")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Calculate",
                  font=("Arial", 11, "bold"), bg="#f0c040", fg="#1a1a2e",
                  padx=12, pady=7, cursor="hand2",
                  command=self.calculate).grid(row=0, column=0, padx=8)

        tk.Button(btn_frame, text="View History",
                  font=("Arial", 11, "bold"), bg="#3498db", fg="white",
                  padx=12, pady=7, cursor="hand2",
                  command=self.show_history).grid(row=0, column=1, padx=8)

        tk.Button(btn_frame, text="Clear",
                  font=("Arial", 11, "bold"), bg="#e74c3c", fg="white",
                  padx=12, pady=7, cursor="hand2",
                  command=self.clear).grid(row=0, column=2, padx=8)

        # ── Result Frame ───────────────────────────────────
        result_frame = tk.Frame(self.root, bg="#16213e", padx=20, pady=20)
        result_frame.pack(pady=20, padx=30, fill="x")

        self.bmi_label = tk.Label(
            result_frame, text="BMI  :  —",
            font=("Arial", 20, "bold"), bg="#16213e", fg="white")
        self.bmi_label.pack()

        self.category_label = tk.Label(
            result_frame, text="Category  :  —",
            font=("Arial", 14), bg="#16213e", fg="white")
        self.category_label.pack(pady=4)

        self.advice_label = tk.Label(
            result_frame, text="",
            font=("Arial", 10, "italic"), bg="#16213e",
            fg="#aaaaaa", wraplength=400)
        self.advice_label.pack()

        # ── Category Reference Bar ─────────────────────────
        ref_frame = tk.Frame(self.root, bg="#1a1a2e")
        ref_frame.pack(pady=8)

        refs = [
            ("< 18.5  Underweight", "#3498db"),
            ("18.5–24.9  Normal",   "#2ecc71"),
            ("25–29.9  Overweight", "#f39c12"),
            ("≥ 30  Obese",         "#e74c3c"),
        ]
        for i, (label, color) in enumerate(refs):
            tk.Label(ref_frame, text=label, font=("Arial", 8),
                     bg="#1a1a2e", fg=color).grid(row=0, column=i, padx=6)

    # ── Calculate Button Logic ─────────────────────────────
    def calculate(self):
        weight_text = self.weight_entry.get().strip()
        height_text = self.height_entry.get().strip()

        # Validate — not empty
        if not weight_text or not height_text:
            messagebox.showerror("Missing Input", "Please fill in both Weight and Height.")
            return

        # Validate — must be numbers
        try:
            weight = float(weight_text)
            height = float(height_text)
        except ValueError:
            messagebox.showerror("Invalid Input",
                                 "Weight and Height must be numbers.\n"
                                 "Example:  Weight = 70   Height = 1.75")
            return

        # Validate — realistic values
        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input",
                                 "Weight and Height must be greater than zero.")
            return

        if height > 3.0:
            messagebox.showerror("Invalid Input",
                                 "Height must be in metres (e.g. 1.75).\n"
                                 "Did you accidentally enter centimetres?")
            return

        if weight > 500:
            messagebox.showerror("Invalid Input",
                                 "Please enter a realistic weight value.")
            return

        # Calculate and display
        bmi      = calculate_bmi(weight, height)
        category, color = get_category(bmi)
        advice   = get_advice(category)

        self.bmi_label.config(text=f"BMI  :  {bmi}", fg=color)
        self.category_label.config(text=f"Category  :  {category}", fg=color)
        self.advice_label.config(text=advice)

        # Save record to history
        record = {
            "date"    : datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
            "weight"  : weight,
            "height"  : height,
            "bmi"     : bmi,
            "category": category,
        }
        self.history.append(record)
        save_history(self.history)

    # ── History Graph Window ───────────────────────────────
    def show_history(self):
        if not self.history:
            messagebox.showinfo("No History",
                                "No records yet.\n"
                                "Calculate your BMI first to start tracking!")
            return

        hist_win = tk.Toplevel(self.root)
        hist_win.title("BMI History Graph")
        hist_win.geometry("720x480")
        hist_win.configure(bg="#1a1a2e")

        dates = [r["date"] for r in self.history]
        bmis  = [r["bmi"]  for r in self.history]

        fig, ax = plt.subplots(figsize=(7, 4), facecolor="#1a1a2e")
        ax.set_facecolor("#16213e")

        # BMI trend line
        ax.plot(dates, bmis, marker="o", color="#f0c040",
                linewidth=2.5, markersize=8, label="Your BMI")

        # WHO reference lines
        ax.axhline(18.5, color="#3498db", linestyle="--",
                   alpha=0.7, label="Underweight limit (18.5)")
        ax.axhline(25.0, color="#f39c12", linestyle="--",
                   alpha=0.7, label="Overweight limit (25.0)")
        ax.axhline(30.0, color="#e74c3c", linestyle="--",
                   alpha=0.7, label="Obese limit (30.0)")

        ax.set_xlabel("Date", color="white", fontsize=9)
        ax.set_ylabel("BMI Value", color="white", fontsize=9)
        ax.set_title("BMI History Over Time",
                     color="#f0c040", fontsize=13, fontweight="bold")
        ax.tick_params(colors="white", labelsize=8)
        ax.tick_params(axis="x", rotation=30)
        for spine in ax.spines.values():
            spine.set_edgecolor("#444444")
        ax.legend(fontsize=8, facecolor="#16213e", labelcolor="white")

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=hist_win)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # ── Clear Button Logic ─────────────────────────────────
    def clear(self):
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.bmi_label.config(text="BMI  :  —", fg="white")
        self.category_label.config(text="Category  :  —", fg="white")
        self.advice_label.config(text="")


# ── Entry Point ───────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
