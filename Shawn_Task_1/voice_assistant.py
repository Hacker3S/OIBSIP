import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time
import sys

# ─────────────────────────────────────────
# Initialize Text-to-Speech Engine
# ─────────────────────────────────────────
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)    # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Initialize the Recognizer globally
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True
recognizer.energy_threshold = 300  

def speak(text):
    """Convert text to speech, print it instantly, and handle engine timing."""
    print(f"Assistant: {text}", flush=True)

    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

    # A tiny pause allows the audio device to close and hand control back to Python
    time.sleep(0.1)


def listen():
    """Listen to the microphone and return recognized text."""
    with sr.Microphone() as source:
        print("\nListening... (speak now)", flush=True)
        
        # Lowering duration to 0.3 so it doesn't hang the loop calibrating silence
        recognizer.adjust_for_ambient_noise(source, duration=0.3)

        try:
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=4)
            print("Processing voice...", flush=True) # Let's you know it heard audio!
            
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}", flush=True)
            return command.lower()

        except sr.WaitTimeoutError:
            # Silent return so it doesn't loop-spam text
            return ""
        except sr.UnknownValueError:
            print("[System: Audio detected but words weren't clear]", flush=True)
            return "ERROR_UNKNOWN"
        except sr.RequestError:
            print("[System: Google API Connection Error]", flush=True)
            return "ERROR_REQUEST"


def process_command(command):
    """Process the recognized voice command."""
    if command == "":
        return True

    if command == "ERROR_UNKNOWN":
        speak("I didn't catch that clearly. Please try again.")
        return True
        
    if command == "ERROR_REQUEST":
        speak("I am having trouble connecting to the internet.")
        return False

    # ── Greeting ──────────────────────────────
    if "hello" in command or "hi" in command:
        speak("Hello! How are you doing today?")

    # ── Current Time ──────────────────────────
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    # ── Current Date ──────────────────────────
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")

    # ── Web Search ────────────────────────────
    elif "search" in command or "google" in command:
        speak("What would you like me to search for?")
        query = listen()
        if query:
            speak(f"Searching for {query}")
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
        else:
            speak("I could not hear your search query. Please try again.")

    # ── Exit ──────────────────────────────────
    elif "exit" in command or "quit" in command or "bye" in command:
        speak("Goodbye!")
        return False

    # ── Unknown Command ───────────────────────
    else:
        speak("Sorry, I did not understand that command.")

    return True


def main():
    """Main function to run the voice assistant."""
    # Force printing of the header layout immediately
    print("=" * 40, flush=True)
    print("   Python Voice Assistant - OIBSIP", flush=True)
    print("   Intern: Shawn Sreeju Sampath", flush=True)
    print("=" * 40, flush=True)
    print("Commands: hello | time | date | search | exit", flush=True)
    print("-" * 40, flush=True)

    speak("Hello! I am your Python Voice Assistant. Say hello, ask the time, date, search something, or say exit to quit.")

    running = True
    while running:
        command = listen()
        running = process_command(command)

    print("\nAssistant stopped. Goodbye!", flush=True)


if __name__ == "__main__":
    main()
