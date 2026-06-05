# ─────────────────────────────────────────────────────────
# Weather App — Oasis Infobyte Internship (Task 4)
# Intern : Shawn Sreeju Sampath | ID: OIB/A2/IP5642
# ─────────────────────────────────────────────────────────

import tkinter as tk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv

# ── Load API key from .env file ───────────────────────────
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ── Weather Icon Mapping ──────────────────────────────────
WEATHER_ICONS = {
    "Clear"        : "☀️",
    "Clouds"       : "☁️",
    "Rain"         : "🌧️",
    "Drizzle"      : "🌦️",
    "Thunderstorm" : "⛈️",
    "Snow"         : "❄️",
    "Mist"         : "🌫️",
    "Fog"          : "🌫️",
    "Haze"         : "🌫️",
    "Smoke"        : "🌫️",
    "Dust"         : "🌫️",
    "Sand"         : "🌫️",
    "Ash"          : "🌫️",
    "Squall"       : "💨",
    "Tornado"      : "🌪️",
}

# ── Background colour per weather condition ───────────────
BG_COLORS = {
    "Clear"        : "#f9a825",
    "Clouds"       : "#546e7a",
    "Rain"         : "#1565c0",
    "Drizzle"      : "#1976d2",
    "Thunderstorm" : "#212121",
    "Snow"         : "#b0bec5",
    "Mist"         : "#607d8b",
    "Fog"          : "#607d8b",
    "Haze"         : "#78909c",
}


# ── Helper Functions ──────────────────────────────────────

def celsius_to_fahrenheit(c):
    return round((c * 9 / 5) + 32, 1)


def fetch_weather(city):
    """
    Fetch weather data from OpenWeatherMap API.
    Returns the parsed JSON dict or raises an exception.
    """
    params = {
        "q"     : city,
        "appid" : API_KEY,
        "units" : "metric",       # always fetch in Celsius
    }
    response = requests.get(BASE_URL, params=params, timeout=10)
    return response


# ── Main Application Class ────────────────────────────────

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App — OIBSIP | Shawn Sreeju Sampath")
        self.root.geometry("480x720")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        # Store last fetched data for unit toggling
        self.last_temp_c   = None
        self.is_celsius    = True

        self.build_ui()

    # ── UI Builder ─────────────────────────────────────────
    def build_ui(self):

        # ── Title ──────────────────────────────────────────
        tk.Label(self.root,
                 text="🌤 Weather App",
                 font=("Arial", 22, "bold"),
                 bg="#1a1a2e", fg="#f0c040").pack(pady=(20, 2))

        tk.Label(self.root,
                 text="Oasis Infobyte Internship  |  Shawn Sreeju Sampath",
                 font=("Arial", 9), bg="#1a1a2e", fg="#777777").pack()

        # ── Search Bar ─────────────────────────────────────
        search_frame = tk.Frame(self.root, bg="#1a1a2e")
        search_frame.pack(pady=20)

        self.city_entry = tk.Entry(
            search_frame,
            font=("Arial", 13), width=22,
            bg="#16213e", fg="white",
            insertbackground="white",
            relief="flat", bd=8)
        self.city_entry.insert(0, "Enter city name...")
        self.city_entry.config(fg="#777777")
        self.city_entry.bind("<FocusIn>",  self.clear_placeholder)
        self.city_entry.bind("<FocusOut>", self.restore_placeholder)
        self.city_entry.bind("<Return>",   lambda e: self.search())
        self.city_entry.pack(side="left", ipady=6)

        tk.Button(search_frame,
                  text="Search",
                  font=("Arial", 12, "bold"),
                  bg="#f0c040", fg="#1a1a2e",
                  padx=12, pady=6,
                  cursor="hand2", relief="flat",
                  command=self.search).pack(side="left", padx=(6, 0))

        # ── Weather Card ───────────────────────────────────
        self.card = tk.Frame(self.root, bg="#16213e",
                             padx=25, pady=25)
        self.card.pack(pady=5, padx=30, fill="x")

        # Weather icon + city name
        self.icon_label = tk.Label(self.card,
                 text="—", font=("Arial", 52),
                 bg="#16213e", fg="white")
        self.icon_label.pack()

        self.city_label = tk.Label(self.card,
                 text="Search for a city above",
                 font=("Arial", 18, "bold"),
                 bg="#16213e", fg="white")
        self.city_label.pack(pady=(4, 0))

        self.condition_label = tk.Label(self.card,
                 text="", font=("Arial", 12, "italic"),
                 bg="#16213e", fg="#aaaaaa")
        self.condition_label.pack()

        # Divider
        tk.Frame(self.card, bg="#333333",
                 height=1).pack(fill="x", pady=14)

        # Temperature display
        self.temp_label = tk.Label(self.card,
                 text="—",
                 font=("Arial", 48, "bold"),
                 bg="#16213e", fg="#f0c040")
        self.temp_label.pack()

        # Toggle button
        self.toggle_btn = tk.Button(self.card,
                 text="Switch to °F",
                 font=("Arial", 10),
                 bg="#0f3460", fg="white",
                 padx=10, pady=4,
                 cursor="hand2", relief="flat",
                 command=self.toggle_unit,
                 state="disabled")
        self.toggle_btn.pack(pady=(4, 14))

        # ── Detail Stats Grid ──────────────────────────────
        stats_frame = tk.Frame(self.card, bg="#16213e")
        stats_frame.pack(fill="x")

        self.stat_labels = {}
        stats = [
            ("💧", "Humidity",    "stat_humidity"),
            ("💨", "Wind Speed",  "stat_wind"),
            ("👁️", "Visibility",  "stat_visibility"),
            ("🌡️", "Feels Like",  "stat_feels"),
        ]

        for i, (icon, title, key) in enumerate(stats):
            row, col = divmod(i, 2)
            box = tk.Frame(stats_frame, bg="#0f3460",
                           padx=14, pady=10)
            box.grid(row=row, column=col,
                     padx=6, pady=6, sticky="nsew")
            stats_frame.columnconfigure(col, weight=1)

            tk.Label(box, text=f"{icon}  {title}",
                     font=("Arial", 9), bg="#0f3460",
                     fg="#aaaaaa").pack(anchor="w")

            lbl = tk.Label(box, text="—",
                     font=("Arial", 13, "bold"),
                     bg="#0f3460", fg="white")
            lbl.pack(anchor="w")
            self.stat_labels[key] = lbl

        # ── Country + Coordinates ──────────────────────────
        self.extra_label = tk.Label(self.root,
                 text="",
                 font=("Arial", 9),
                 bg="#1a1a2e", fg="#555555")
        self.extra_label.pack(pady=(10, 0))

        # ── Status Bar ─────────────────────────────────────
        self.status_label = tk.Label(self.root,
                 text="Powered by OpenWeatherMap API",
                 font=("Arial", 8),
                 bg="#1a1a2e", fg="#444444")
        self.status_label.pack(pady=(4, 10))

    # ── Placeholder Helpers ────────────────────────────────
    def clear_placeholder(self, event):
        if self.city_entry.get() == "Enter city name...":
            self.city_entry.delete(0, tk.END)
            self.city_entry.config(fg="white")

    def restore_placeholder(self, event):
        if not self.city_entry.get():
            self.city_entry.insert(0, "Enter city name...")
            self.city_entry.config(fg="#777777")

    # ── Search Logic ───────────────────────────────────────
    def search(self):
        city = self.city_entry.get().strip()

        if not city or city == "Enter city name...":
            messagebox.showwarning("Missing Input",
                                   "Please enter a city name.")
            return

        self.status_label.config(text="Fetching weather data...",
                                 fg="#f0c040")
        self.root.update()

        try:
            response = fetch_weather(city)

            # ── City not found ─────────────────────────────
            if response.status_code == 404:
                messagebox.showerror("City Not Found",
                    f"'{city}' was not found.\n"
                    "Please check the spelling and try again.")
                self.status_label.config(
                    text="City not found.", fg="#e74c3c")
                return

            # ── Invalid API key ────────────────────────────
            if response.status_code == 401:
                messagebox.showerror("Invalid API Key",
                    "Your API key is invalid or not yet active.\n"
                    "New keys take 10–30 minutes to activate.\n"
                    "Check your .env file.")
                self.status_label.config(
                    text="API key error.", fg="#e74c3c")
                return

            # ── Other API errors ───────────────────────────
            if response.status_code != 200:
                messagebox.showerror("API Error",
                    f"Unexpected error: {response.status_code}\n"
                    "Please try again later.")
                return

            data = response.json()
            self.display_weather(data)
            self.status_label.config(
                text="Data fetched successfully ✅",
                fg="#2ecc71")

        except requests.exceptions.ConnectionError:
            messagebox.showerror("No Internet",
                                 "Could not connect to the internet.\n"
                                 "Please check your network connection.")
            self.status_label.config(text="Network error.", fg="#e74c3c")

        except requests.exceptions.Timeout:
            messagebox.showerror("Timeout",
                                 "The request took too long.\n"
                                 "Please check your connection and try again.")
            self.status_label.config(text="Request timed out.", fg="#e74c3c")

    # ── Display Weather Data ───────────────────────────────
    def display_weather(self, data):
        # Extract values from JSON
        city_name   = data["name"]
        country     = data["sys"]["country"]
        condition   = data["weather"][0]["main"]
        description = data["weather"][0]["description"].title()
        temp_c      = round(data["main"]["temp"], 1)
        feels_c     = round(data["main"]["feels_like"], 1)
        humidity    = data["main"]["humidity"]
        wind_speed  = data["wind"]["speed"]
        visibility  = data.get("visibility", 0) // 1000  # m → km
        lat         = data["coord"]["lat"]
        lon         = data["coord"]["lon"]

        # Store celsius value for toggle
        self.last_temp_c  = temp_c
        self.last_feels_c = feels_c
        self.is_celsius   = True

        # Icon and background
        icon    = WEATHER_ICONS.get(condition, "🌡️")
        bg_col  = BG_COLORS.get(condition, "#16213e")

        # Update card background
        self.card.config(bg=bg_col)
        
        # Safely update main card elements without destroying sub-grid colors
        labels_to_update = [self.icon_label, self.city_label, self.condition_label, self.temp_label]
        for label in labels_to_update:
            label.config(bg=bg_col)

        # Update text metrics
        self.icon_label.config(text=icon)
        self.city_label.config(text=f"{city_name}, {country}")
        self.condition_label.config(text=description)
        self.temp_label.config(text=f"{temp_c} °C")
        self.toggle_btn.config(text="Switch to °F", state="normal", bg="#0f3460")

        # Stat boxes
        self.stat_labels["stat_humidity"].config(text=f"{humidity} %")
        self.stat_labels["stat_wind"].config(text=f"{wind_speed} m/s")
        self.stat_labels["stat_visibility"].config(text=f"{visibility} km")
        self.stat_labels["stat_feels"].config(text=f"{feels_c} °C")

        self.extra_label.config(text=f"📍 Lat: {lat}  |  Lon: {lon}")

    # ── Unit Toggle ────────────────────────────────────────
    def toggle_unit(self):
        if self.last_temp_c is None:
            return

        if self.is_celsius:
            # Switch to Fahrenheit
            temp_f   = celsius_to_fahrenheit(self.last_temp_c)
            feels_f  = celsius_to_fahrenheit(self.last_feels_c)
            self.temp_label.config(text=f"{temp_f} °F")
            self.stat_labels["stat_feels"].config(text=f"{feels_f} °F")
            self.toggle_btn.config(text="Switch to °C")
            self.is_celsius = False
        else:
            # Switch back to Celsius
            self.temp_label.config(text=f"{self.last_temp_c} °C")
            self.stat_labels["stat_feels"].config(text=f"{self.last_feels_c} °C")
            self.toggle_btn.config(text="Switch to °F")
            self.is_celsius = True


# ── Entry Point ───────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
