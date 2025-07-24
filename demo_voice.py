import tkinter as tk
from tkinter import messagebox, scrolledtext
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    try:
        # Try default microphone
        with sr.Microphone() as source:
            status_label.config(text="🎤 Listening... Speak now.")
            root.update()
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5)

        status_label.config(text="🔍 Recognizing...")
        root.update()

        # Convert speech to text using Google
        text = recognizer.recognize_google(audio, language='en-IN')
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, text)

        # Save to file
        with open("output.txt", "w") as f:
            f.write(text)

        status_label.config(text="✅ Speech recognized and saved to output.txt.")

    except sr.WaitTimeoutError:
        messagebox.showerror("Timeout", "⏰ You didn't speak in time.")
    except sr.UnknownValueError:
        messagebox.showerror("Error", "😕 Couldn't understand your voice.")
    except sr.RequestError as e:
        messagebox.showerror("API Error", f"❌ Google Speech API error: {e}")
    except OSError as e:
        messagebox.showerror("Microphone Error", f"🎙️ Mic issue: {e}")
    except Exception as e:
        messagebox.showerror("Unexpected Error", str(e))


# GUI Setup
root = tk.Tk()
root.title("🎤 Voice Recognition - Speech to Text")
root.geometry("550x400")
root.resizable(False, False)

title = tk.Label(root, text="Speech to Text Converter", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

status_label = tk.Label(root, text="Click the button and start speaking.", font=("Arial", 12))
status_label.pack(pady=10)

start_button = tk.Button(root, text="🎧 Start Listening", command=recognize_speech,
                         font=("Arial", 12), bg="#4CAF50", fg="white")
start_button.pack(pady=10)

result_box = scrolledtext.ScrolledText(root, height=10, width=60, wrap=tk.WORD, font=("Arial", 11))
result_box.pack(pady=10)

root.mainloop()
