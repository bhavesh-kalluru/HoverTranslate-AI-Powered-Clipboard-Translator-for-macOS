# 🚀 HoverTranslate – AI-Powered Clipboard Translator for macOS

HoverTranslate is a lightweight, privacy-friendly macOS menu bar app that automatically translates any copied text into your selected language using OpenAI’s GPT-4.

⚡ No clicking needed.  
🌍 No Google or Apple Translate.  
🍎 Designed just for macOS.

---

### ✨ Features

- 📋 **Clipboard Monitoring** – Automatically detects copied text
- 🌍 **Language Selection** – Translate to Spanish, Hindi, or French
- 💬 **GPT-4 Powered** – Natural and context-aware translations
- 🔔 **Native Notifications** – No intrusive popups or UI crashes
- ✅ **Offline-Friendly UI** – No tkinter or bloated GUI libraries
- ❌ **No External Translate APIs** – 100% OpenAI-based

---

### 🔧 Installation

1. **Clone the repo**
   git clone https://github.com/your-username/HoverTranslate.git
   cd HoverTranslate

2. Install dependencies
   pip install -r requirements.txt
   Set your OpenAI API key

3.Create a .env file:
  OPENAI_API_KEY=your-openai-key-here
 
  Run the app
  python -m src.main
  
🗣️ Supported Languages
Currently supported target languages:
🇪🇸 Spanish
🇮🇳 Hindi
🇫🇷 French
(OpenAI automatically detects the source language.)

🛠 Project Structure
css
Copy
Edit
HoverTranslate/
├── .env
├── requirements.txt
└── src/
    ├── main.py
    ├── ui/
    │   ├── __init__.py
    │   └── menu.py
    └── translate/
        ├── __init__.py
        └── engine.py

🙌 Credits
Built by @kallurubhavesh341 using:
rumps
OpenAI GPT-4
pyperclip

📃 License
MIT License — free for personal and commercial use.

with you

You're almost ready for launch! 🚀
