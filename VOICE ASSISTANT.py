import tkinter as tk
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random

# Initialize pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
engine.setProperty('voice', engine.getProperty('voices')[1].id)

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        status_label.config(text="Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        command_display.insert(tk.END, f"You said: {command}\n")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        status_label.config(text="Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        speak("Check your internet connection.")
        status_label.config(text="Check your internet connection.")
        return None

# Command execution
def execute_command(command):
    if 'hello' in command:
        respond("Hello! I am Aura. How may I help you?")
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        respond(f"The current time is {current_time}")
    elif 'open youtube' in command:
        open_website('https://www.youtube.com', "Opening YouTube.")
    elif 'open google' in command:
        open_website('https://www.google.com', "Opening Google.")
    elif 'search for' in command:
        query = command.replace('search for', '').strip()
        if query:
            open_website(f'https://www.google.com/search?q={query}', f"Searching for {query} on Google.")
        else:
            respond("What should I search for?")
    elif 'play music' in command:
        play_random_music()
    elif 'open notepad' in command:
        open_application("notepad", "Opening Notepad.")
    elif 'open calculator' in command:
        open_application("calc", "Opening Calculator.")
    elif 'dark mode' in command:
        toggle_mode('dark')
    elif 'light mode' in command:
        toggle_mode('light')
    elif 'exit' in command or 'quit' in command:
        respond("Goodbye!")
        root.quit()
    else:
        respond("Sorry, I don't understand that command.")

# Respond utility
def respond(message):
    speak(message)
    status_label.config(text=message)

# Open website utility
def open_website(url, message):
    webbrowser.open(url)
    respond(message)

# Open application utility
def open_application(command, message):
    os.system(command)
    respond(message)

# Play music utility
def play_random_music():
    music_folder = "C:/music"
    songs = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
    if songs:
        song_to_play = os.path.join(music_folder, random.choice(songs))
        os.startfile(song_to_play)
        respond(f"Playing {os.path.basename(song_to_play)}.")
    else:
        respond("No music files found in the folder.")

# Toggle dark/light mode
def toggle_mode(mode=None):
    if mode == 'dark' or root.cget("bg") == 'white':
        update_theme('black', 'white', "Dark mode activated.", "Switch to Light Mode")
    elif mode == 'light' or root.cget("bg") == 'black':
        update_theme('white', 'black', "Light mode activated.", "Switch to Dark Mode")

# Update theme utility
def update_theme(bg_color, fg_color, speak_message, button_text):
    root.config(bg=bg_color)
    greeting_label.config(bg=bg_color, fg=fg_color)
    commands_label.config(bg=bg_color, fg=fg_color)
    status_label.config(bg=bg_color, fg=fg_color)
    command_display.config(bg=bg_color, fg=fg_color)
    mode_button.config(text=button_text, bg=bg_color, fg=fg_color)
    speak(speak_message)

# Start assistant
def start_assistant():
    command_display.delete('1.0', tk.END)
    respond("Listening...")
    command = listen()
    if command:
        execute_command(command)

# GUI setup
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("800x600")
root.config(bg='white')

greeting_label = tk.Label(root, text="Hey there! I am Aura, your personal Voice Assistant!", font=("Arial", 16), bg='white', fg='black')
greeting_label.pack(pady=20)

commands_label = tk.Label(
    root,
    text="Try these commands:\n'hello', 'time', 'open youtube', 'open google', 'search for [something]', 'play music', 'open notepad', 'open calculator', 'dark mode', 'light mode', 'exit'",
    font=("Arial", 14),
    bg='white',
    fg='black',
    justify="center"
)
commands_label.pack(pady=20)

status_label = tk.Label(root, text="Press 'Start' to begin", font=("Arial", 14), bg='white', fg='black')
status_label.pack(pady=20)

command_display = tk.Text(root, font=("Arial", 12), bg='white', fg='black', height=10, width=60)
command_display.pack(pady=20)
command_display.insert(tk.END, "Your commands will appear here...\n")

start_button = tk.Button(root, text="Start Listening", font=("Arial", 14), command=start_assistant, bg='blue', fg='white')
start_button.pack(pady=10)

mode_button = tk.Button(root, text="Switch to Dark Mode", font=("Arial", 14), command=toggle_mode, bg='white', fg='black')
mode_button.pack(pady=10)

root.mainloop()
