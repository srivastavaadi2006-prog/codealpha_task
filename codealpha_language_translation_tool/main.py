import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip  # Built into tkinter/standard environments for copying text
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import threading

# Initialize main window
root = tk.Tk()
root.title("CodeAlpha - Language Translation Tool")
root.geometry("600x500")
root.configure(bg="#f4f6f9")

# Supported Languages Dictionary
LANGUAGES = {
    'English': 'en',
    'Hindi': 'hi',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Arabic': 'ar',
    'Chinese (Simplified)': 'zh-CN',
    'Japanese': 'ja',
    'Russian': 'ru'
}

# --- Translation Logic Functions ---

def translate_text():
    """Handles the translation process."""
    source_text = src_text_box.get("1.0", tk.END).strip()
    src_lang = src_lang_combo.get()
    dest_lang = dest_lang_combo.get()

    if not source_text:
        messagebox.showwarning("Input Error", "Please enter some text to translate.")
        return

    try:
        # Fetch language codes
        src_code = LANGUAGES[src_lang]
        dest_code = LANGUAGES[dest_lang]
        
        # Perform Translation
        translated = GoogleTranslator(source=src_code, target=dest_code).translate(source_text)
        
        # Display Output
        dest_text_box.delete("1.0", tk.END)
        dest_text_box.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Translation Error", f"Something went wrong: {str(e)}")

def copy_to_clipboard():
    """Copies translated text to clipboard."""
    translated_text = dest_text_box.get("1.0", tk.END).strip()
    if translated_text:
        pyperclip.copy(translated_text)
        messagebox.showinfo("Success", "Translated text copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "Nothing to copy yet.")

def speak_text_thread():
    """Runs Text-to-Speech in a background thread to keep UI responsive."""
    translated_text = dest_text_box.get("1.0", tk.END).strip()
    dest_lang = dest_lang_combo.get()
    
    if not translated_text:
        messagebox.showwarning("Empty", "No text to speak.")
        return
        
    try:
        dest_code = LANGUAGES[dest_lang]
        tts = gTTS(text=translated_text, lang=dest_code, slow=False)
        tts.save("captured_voice.mp3")
        
        # Play the audio file depending on OS
        if os.name == 'nt': # Windows
            os.system("start captured_voice.mp3")
        else: # Mac/Linux
            os.system("afplay captured_voice.mp3" if os.uname().sysname == 'Darwin' else "xdg-open captured_voice.mp3")
    except Exception as e:
        messagebox.showerror("Audio Error", f"Could not play audio: {str(e)}")

def trigger_speak():
    # Using thread prevents UI freezing while audio generates
    threading.Thread(target=speak_text_thread, daemon=True).start()

# --- UI Layout Design ---

# Title Banner
title_label = tk.Label(root, text="Language Translation Tool", font=("Arial", 18, "bold"), fg="#2c3e50", bg="#f4f6f9")
title_label.pack(pady=10)

# Frame for Selectors
select_frame = tk.Frame(root, bg="#f4f6f9")
select_frame.pack(pady=10)

tk.Label(select_frame, text="From:", font=("Arial", 10, "bold"), bg="#f4f6f9").grid(row=0, column=0, padx=5)
src_lang_combo = ttk.Combobox(select_frame, values=list(LANGUAGES.keys()), state="readonly", width=15)
src_lang_combo.grid(row=0, column=1, padx=10)
src_lang_combo.set('English')

tk.Label(select_frame, text="To:", font=("Arial", 10, "bold"), bg="#f4f6f9").grid(row=0, column=2, padx=5)
dest_lang_combo = ttk.Combobox(select_frame, values=list(LANGUAGES.keys()), state="readonly", width=15)
dest_lang_combo.grid(row=0, column=3, padx=10)
dest_lang_combo.set('Hindi')

# Input Text Box
tk.Label(root, text="Enter Text:", font=("Arial", 10, "bold"), bg="#f4f6f9").pack(anchor="w", padx=40)
src_text_box = tk.Text(root, height=5, width=60, font=("Arial", 11))
src_text_box.pack(pady=5)

# Translate Button
translate_btn = tk.Button(root, text="Translate", font=("Arial", 11, "bold"), bg="#3498db", fg="white", bd=0, padx=20, pady=5, command=translate_text)
translate_btn.pack(pady=10)

# Output Text Box
tk.Label(root, text="Translated Text:", font=("Arial", 10, "bold"), bg="#f4f6f9").pack(anchor="w", padx=40)
dest_text_box = tk.Text(root, height=5, width=60, font=("Arial", 11), bg="#ecf0f1")
dest_text_box.pack(pady=5)

# Features Button Frame (Copy & Audio)
btn_frame = tk.Frame(root, bg="#f4f6f9")
btn_frame.pack(pady=15)

copy_btn = tk.Button(btn_frame, text="📋 Copy", font=("Arial", 10), bg="#2ecc71", fg="white", bd=0, padx=15, pady=5, command=copy_to_clipboard)
copy_btn.grid(row=0, column=0, padx=10)

speak_btn = tk.Button(btn_frame, text="🔊 Listen", font=("Arial", 10), bg="#e67e22", fg="white", bd=0, padx=15, pady=5, command=trigger_speak)
speak_btn.grid(row=0, column=1, padx=10)

# Footer
footer = tk.Label(root, text="CodeAlpha AI Internship Project", font=("Arial", 8, "italic"), fg="#7f8c8d", bg="#f4f6f9")
footer.pack(side="bottom", pady=5)

root.mainloop()