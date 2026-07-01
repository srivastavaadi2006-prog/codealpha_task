# CodeAlpha: Language Translation Tool

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Domain](https://img.shields.io/badge/Domain-Artificial%20Intelligence-orange)

An interactive, desktop-based **Language Translation Tool** built from scratch using Python, Tkinter, and the Google Translate API (via the `deep-translator` engine). This project is developed as part of the **CodeAlpha Artificial Intelligence Internship** program.

---

## 🚀 Features

- **Multi-Language Support:** Seamless translation across major global and regional languages (English, Hindi, Spanish, French, German, Arabic, Chinese, Japanese, Russian).
- **User-Friendly GUI:** Clean, responsive desktop interface built entirely using Python's `tkinter` and `ttk` libraries.
- **One-Click Clipboard Copy:** Integrated functionality to instantly copy the translated output with a single click.
- **Text-to-Speech (TTS) Integration:** Audio playback button using `gTTS` that reads out the translated text in its native accent natively.
- **Multi-Threaded Architecture:** Audio processing handles complex API calls via background threads, keeping the core window responsive without freezes.

---

## 🛠️ Tech Stack & Dependencies

- **Core Language:** Python 3.8+
- **GUI Framework:** Tkinter (Standard Library)
- **Translation Engine:** `deep-translator` (Interactions with Google Translate API)
- **Speech Synthesis:** `gTTS` (Google Text-to-Speech)
- **Clipboard Utility:** `pyperclip`

---

## 📦 Installation & Setup

Follow these steps to run the application locally on your machine:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)[adityaRALPH]/CodeAlpha_Language_Translation_Tool.git
   cd CodeAlpha_Language_Translation_Tool

*Note for Linux Users: If clipboard copy actions throw an environment error, run 'sudo apt-get install xclip' to enable clipboard support.*