# ─────────────────────────────────────────────────────────
# Random Password Generator — Oasis Infobyte Internship (Task 3)
# Intern : Shawn Sreeju Sampath | ID: OIB/A2/IP5642
# ─────────────────────────────────────────────────────────

import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string
import pyperclip

# ── Constants ─────────────────────────────────────────────
UPPERCASE = string.ascii_uppercase   # A-Z
LOWERCASE = string.ascii_lowercase   # a-z
DIGITS    = string.digits            # 0-9
SYMBOLS   = string.punctuation       # !@#$%^&*...


# ── Helper Functions ──────────────────────────────────────

def build_character_pool(use_upper, use_lower, use_digits, use_symbols):
    """Build the character pool based on user's checkbox selections."""
    pool = ""
    if use_upper:   pool += UPPERCASE
    if use_lower:   pool += LOWERCASE
    if use_digits:  pool += DIGITS
    if use_symbols: pool += SYMBOLS
    return pool


def generate_password(length, pool):
    """Generate a cryptographically secure random password."""
    return "".join(secrets.choice(pool) for _ in range(length))


def get_strength(password, use_upper, use_lower, use_digits, use_symbols):
    """
    Rate password strength based on length and character diversity.
    Returns: (label, color, progress_value)
    """
    score = 0
    if use_upper:            score += 1
    if use_lower:            score += 1
    if use_digits:           score += 1
    if use_symbols:          score += 1
    if len(password) >= 12:  score += 1
    if len(password) >= 16:  score += 1

    if score <= 2:
        return "Weak",      "#e74c3c", 25
    elif score == 3:
        return "Fair",      "#f39c12", 50
    elif score == 4:
        return "Strong",    "#2ecc71", 75
    else:
        return "Very Strong","#27ae60", 100


# ── Main Application Class ────────────────────────────────

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator — OIBSIP | Shawn Sreeju Sampath")
        self.root.geometry("520x680")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        # Tkinter variables
        self.length_var    = tk.IntVar(value=12)
        self.upper_var     = tk.BooleanVar(value=True)
        self.lower_var     = tk.BooleanVar(value=True)
        self.digits_var    = tk.BooleanVar(value=True)
        self.symbols_var   = tk.BooleanVar(value=True)
        self.password_var  = tk.StringVar(value="")

        self.build_ui()

    # ── UI Builder ─────────────────────────────────────────
    def build_ui(self):

        # ── Title ──────────────────────────────────────────
        tk.Label(self.root,
                 text="🔐  Password Generator",
                 font=("Arial", 22, "bold"),
                 bg="#1a1a2e", fg="#f0c040").pack(pady=(20, 2))

        tk.Label(self.root,
                 text="Oasis Infobyte Internship  |  Shawn Sreeju Sampath",
                 font=("Arial", 9), bg="#1a1a2e", fg="#777777").pack()

        # ── Length Slider Section ──────────────────────────
        slider_frame = tk.Frame(self.root, bg="#16213e", padx=25, pady=18)
        slider_frame.pack(pady=18, padx=30, fill="x")

        # Header row: label + live counter
        top_row = tk.Frame(slider_frame, bg="#16213e")
        top_row.pack(fill="x")

        tk.Label(top_row, text="Password Length",
                 font=("Arial", 12, "bold"),
                 bg="#16213e", fg="white").pack(side="left")

        self.length_display = tk.Label(top_row,
                 text="12", font=("Arial", 14, "bold"),
                 bg="#16213e", fg="#f0c040")
        self.length_display.pack(side="right")

        # Slider
        self.slider = ttk.Scale(
            slider_frame,
            from_=6, to=32,
            orient="horizontal",
            variable=self.length_var,
            command=self.on_slider_move)
        self.slider.pack(fill="x", pady=(8, 2))

        # Min / Max labels
        minmax = tk.Frame(slider_frame, bg="#16213e")
        minmax.pack(fill="x")
        tk.Label(minmax, text="6",  font=("Arial", 8),
                 bg="#16213e", fg="#666666").pack(side="left")
        tk.Label(minmax, text="32", font=("Arial", 8),
                 bg="#16213e", fg="#666666").pack(side="right")

        # ── Character Options ──────────────────────────────
        options_frame = tk.Frame(self.root, bg="#16213e", padx=25, pady=18)
        options_frame.pack(padx=30, fill="x")

        tk.Label(options_frame, text="Include Characters",
                 font=("Arial", 12, "bold"),
                 bg="#16213e", fg="white").grid(
                 row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        checkboxes = [
            ("Uppercase  (A – Z)",  self.upper_var),
            ("Lowercase  (a – z)",  self.lower_var),
            ("Numbers   (0 – 9)",   self.digits_var),
            ("Symbols   (!@#$...)", self.symbols_var),
        ]

        style = ttk.Style()
        style.configure("Custom.TCheckbutton",
                        background="#16213e",
                        foreground="white",
                        font=("Arial", 11))

        for i, (label, var) in enumerate(checkboxes):
            row, col = divmod(i, 2)
            ttk.Checkbutton(
                options_frame, text=label,
                variable=var,
                style="Custom.TCheckbutton").grid(
                row=row + 1, column=col,
                sticky="w", padx=10, pady=5)

        # ── Generate Button ────────────────────────────────
        tk.Button(self.root,
                  text="⚡  Generate Password",
                  font=("Arial", 13, "bold"),
                  bg="#f0c040", fg="#1a1a2e",
                  padx=20, pady=10,
                  cursor="hand2",
                  relief="flat",
                  command=self.generate).pack(pady=18)

        # ── Password Display Box ───────────────────────────
        display_frame = tk.Frame(self.root, bg="#16213e", padx=20, pady=15)
        display_frame.pack(padx=30, fill="x")

        tk.Label(display_frame, text="Generated Password",
                 font=("Arial", 10), bg="#16213e",
                 fg="#888888").pack(anchor="w")

        self.password_display = tk.Entry(
            display_frame,
            textvariable=self.password_var,
            font=("Courier", 13, "bold"),
            bg="#0f3460", fg="#f0c040",
            insertbackground="#f0c040",
            relief="flat", bd=8,
            state="readonly",
            readonlybackground="#0f3460",
            justify="center")
        self.password_display.pack(fill="x", pady=(6, 0))

        # ── Strength Bar ───────────────────────────────────
        strength_frame = tk.Frame(self.root, bg="#1a1a2e", padx=30)
        strength_frame.pack(fill="x", pady=(12, 0), padx=30)

        str_row = tk.Frame(strength_frame, bg="#1a1a2e")
        str_row.pack(fill="x")

        tk.Label(str_row, text="Strength:",
                 font=("Arial", 10), bg="#1a1a2e",
                 fg="#aaaaaa").pack(side="left")

        self.strength_label = tk.Label(str_row, text="—",
                 font=("Arial", 10, "bold"),
                 bg="#1a1a2e", fg="white")
        self.strength_label.pack(side="left", padx=6)

        self.strength_bar = ttk.Progressbar(
            strength_frame,
            orient="horizontal",
            length=440, mode="determinate")
        self.strength_bar.pack(fill="x", pady=(4, 0))

        # ── Action Buttons ─────────────────────────────────
        action_frame = tk.Frame(self.root, bg="#1a1a2e")
        action_frame.pack(pady=18)

        tk.Button(action_frame,
                  text="📋  Copy to Clipboard",
                  font=("Arial", 11, "bold"),
                  bg="#3498db", fg="white",
                  padx=14, pady=8,
                  cursor="hand2", relief="flat",
                  command=self.copy_password).grid(
                  row=0, column=0, padx=10)

        tk.Button(action_frame,
                  text="🔄  New Password",
                  font=("Arial", 11, "bold"),
                  bg="#2ecc71", fg="white",
                  padx=14, pady=8,
                  cursor="hand2", relief="flat",
                  command=self.generate).grid(
                  row=0, column=1, padx=10)

        tk.Button(action_frame,
                  text="🗑  Clear",
                  font=("Arial", 11, "bold"),
                  bg="#e74c3c", fg="white",
                  padx=14, pady=8,
                  cursor="hand2", relief="flat",
                  command=self.clear).grid(
                  row=0, column=2, padx=10)

        # ── Tips Label ─────────────────────────────────────
        tk.Label(self.root,
                 text="💡 Uses Python's secrets module for cryptographic security",
                 font=("Arial", 8, "italic"),
                 bg="#1a1a2e", fg="#555555").pack(pady=(0, 10))

    # ── Slider Move Handler ────────────────────────────────
    def on_slider_move(self, value):
        """Update the length counter label as slider moves."""
        self.length_display.config(text=str(int(float(value))))

    # ── Generate Button Logic ──────────────────────────────
    def generate(self):
        use_upper   = self.upper_var.get()
        use_lower   = self.lower_var.get()
        use_digits  = self.digits_var.get()
        use_symbols = self.symbols_var.get()

        # Validate — at least one type must be selected
        if not any([use_upper, use_lower, use_digits, use_symbols]):
            messagebox.showerror(
                "No Character Type Selected",
                "Please select at least one character type\n"
                "(Uppercase, Lowercase, Numbers, or Symbols).")
            return

        length   = self.length_var.get()
        pool     = build_character_pool(use_upper, use_lower,
                                        use_digits, use_symbols)
        password = generate_password(length, pool)

        self.password_var.set(password)

        # Update strength bar
        label, color, value = get_strength(
            password, use_upper, use_lower, use_digits, use_symbols)

        self.strength_label.config(text=label, fg=color)
        self.strength_bar["value"] = value

    # ── Copy to Clipboard ──────────────────────────────────
    def copy_password(self):
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("No Password",
                                   "Generate a password first!")
            return
        pyperclip.copy(password)
        messagebox.showinfo("Copied! ✅",
                            "Password copied to clipboard successfully!")

    # ── Clear Button Logic ─────────────────────────────────
    def clear(self):
        self.password_var.set("")
        self.strength_label.config(text="—", fg="white")
        self.strength_bar["value"] = 0


# ── Entry Point ───────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
