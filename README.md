🤖 Jarvis AI Assistant

A futuristic offline + online AI voice assistant built with Python for Windows 11.

Jarvis can:

- Listen to voice commands
- Speak responses
- Open apps and websites
- Control Windows features
- Work offline using Vosk speech recognition
- Start automatically with Windows

---

🚀 Features

- Offline voice recognition using Vosk
- Text-to-speech assistant
- Wake word detection ("Jarvis")
- Windows app launcher
- Website opener
- Media controls
- Fast response system
- Offline functionality
- Startup automation
- EXE build support using PyInstaller

---

🎤 Supported Commands

🌐 Web Commands

- Jarvis open Google
- Jarvis open YouTube
- Jarvis open GitHub
- Jarvis open ChatGPT

💻 Windows Apps

- Jarvis open calculator
- Jarvis open notepad
- Jarvis open paint
- Jarvis open terminal
- Jarvis open settings
- Jarvis open task manager
- Jarvis open camera
- Jarvis open media player

🎵 Media Controls

- Jarvis play music
- Jarvis pause music
- Jarvis next song
- Jarvis previous song

⚙️ Utility Commands

- Jarvis what is the time
- Jarvis what is today's date
- Jarvis stop

---

🛠️ Technologies Used

- Python
- Vosk
- SpeechRecognition
- pywin32
- PyAudio
- PyAutoGUI
- Requests
- PyInstaller

---

⚡ Installation

1️⃣ Clone Repository

git clone https://github.com/adarsh399/Jarvis-AI.git
cd Jarvis-AI

---

2️⃣ Install Dependencies

py -3.12 -m pip install -r requirements.txt

---

🎙️ Download Offline Speech Model

Download a Vosk model from:

https://alphacephei.com/vosk/models

Recommended model:

vosk-model-small-en-us-0.15

Rename the downloaded folder to:

model

Place it inside the project folder.

---

▶️ Run Jarvis

py -3.12 main.py

---

🔥 Build EXE File

py -3.12 -m PyInstaller --onefile --noconsole --collect-all vosk --add-data "model;model" main.py

The EXE file will appear inside:

dist/

---

⚙️ Auto Start with Windows

1. Create shortcut of "Jarvis.exe"
2. Press "WIN + R"
3. Type:

shell:startup

4. Paste shortcut into the Startup folder

Now Jarvis will launch automatically when Windows starts.

---

📁 Project Structure

Jarvis-AI/
│
├── main.py
├── requirements.txt
├── model/
├── README.md
├── build/
└── dist/

---

💡 Future Improvements

- ChatGPT integration
- Face recognition
- GUI interface
- Smart home controls
- AI memory system
- Mobile app integration

---

👨‍💻 Created By

Adarsh Kumar

---

📄 License

This project is open-source and free to use.
