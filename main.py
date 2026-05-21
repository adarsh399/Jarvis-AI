import webbrowser
import os
import requests
from dotenv import load_dotenv
import subprocess
from datetime import datetime

import speech_recognition as sr
import win32com.client


# =========================
# LOAD ENV
# =========================

load_dotenv()

API_KEY = os.getenv("DEEPSEEK_API_KEY")
MODEL = os.getenv("DEEPSEEK_MODEL")


# =========================
# SETUP
# =========================

recognizer = sr.Recognizer()

speaker = win32com.client.Dispatch("SAPI.SpVoice")

speaker.Rate = 2

WAKE_WORD = "jarvis"


# =========================
# SPEAK FUNCTION
# =========================

def speak(text):

    try:

        print(f"\nJarvis: {text}")

        speaker.Speak(str(text))

    except Exception as e:

        print("Speaker Error:", e)


# =========================
# LISTEN FUNCTION
# =========================

def listen():

    try:

        with sr.Microphone() as source:

            recognizer.energy_threshold = 300
            recognizer.pause_threshold = 0.5
            recognizer.dynamic_energy_threshold = True

            print("\nListening...")

            audio = recognizer.listen(
                source,
                timeout=3,
                phrase_time_limit=4
            )

        print("Recognizing...")

        text = recognizer.recognize_google(audio)

        text = text.lower().strip()

        print("You said:", text)

        return text

    except sr.WaitTimeoutError:

        return ""

    except sr.UnknownValueError:

        print("Could not understand")

        return ""

    except Exception as e:

        print("Error:", e)

        return ""


# =========================
# AI FUNCTION
# =========================

def ask_ai(question):

    try:

        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "You are Jarvis, a futuristic AI assistant."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        }

        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=30
        )

        result = response.json()

        print(result)

        return result["choices"][0]["message"]["content"]

    except Exception as e:

        print("AI Error:", e)

        return "Sorry, AI connection failed."


# =========================
# COMMAND HANDLER
# =========================

def handle_command(command):

    command = command.lower().strip()

    command = command.replace("jariva", "")
    command = command.replace("jarivs", "")
    command = command.replace("jarvis", "")

    command = command.strip()

    # -------------------------

    if "youtube" in command:

        webbrowser.open("https://youtube.com")

        return "Opening YouTube"

    # -------------------------

    if "google" in command:

        webbrowser.open("https://google.com")

        return "Opening Google"

    # -------------------------

    if "chatgpt" in command:

        webbrowser.open("https://chat.openai.com")

        return "Opening ChatGPT"

    # -------------------------

    if "notepad" in command:

        subprocess.Popen("notepad.exe")

        return "Opening Notepad"

    # -------------------------

    if "calculator" in command:

        subprocess.Popen("calc.exe")

        return "Opening Calculator"

    # -------------------------

    if "paint" in command:

        subprocess.Popen("mspaint.exe")

        return "Opening Paint"

    # -------------------------

    if "time" in command:

        now = datetime.now().strftime("%I:%M %p")

        return f"The time is {now}"

    # -------------------------

    if "date" in command:

        today = datetime.now().strftime("%d %B %Y")

        return f"Today's date is {today}"

    # -------------------------

    if "shutdown" in command:

        return "Shutdown blocked for safety"

    # -------------------------

    return None


# =========================
# MAIN LOOP
# =========================

def main():

    print("=================================")
    print("         JARVIS AI ONLINE")
    print("=================================")

    speak("Jarvis online")

    while True:

        text = listen()

        if not text:
            continue

        # Stop command
        if "jarvis stop" in text or "goodbye" in text:

            speak("Goodbye")

            break

        # Remove wake word
        if WAKE_WORD in text:

            command = text.replace(
                WAKE_WORD,
                ""
            ).strip()

        else:

            command = text.strip()

        print("Command:", command)

        # Local commands
        reply = handle_command(command)

        # If local command exists
        if reply:

            speak(reply)

        # Otherwise AI
        else:

            print("Sending to AI...")

            ai_reply = ask_ai(command)

            print("AI Reply:", ai_reply)

            speak(ai_reply)


# =========================
# START
# =========================

if __name__ == "__main__":

    main()