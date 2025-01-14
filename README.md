Voice Assistant GUI

A Python-based Voice Assistant with a graphical user interface built using Tkinter. It integrates speech recognition, text-to-speech, and executes various commands like opening websites, applications, and more.

Features
Speech Recognition: Understands and processes voice commands.
Text-to-Speech: Responds to commands using a natural-sounding voice.

Command Execution:
Open websites (e.g., YouTube, Google).
Search the web.
Launch applications (Notepad, Calculator).
Play music from a specified folder.
Toggle between light and dark mode.
User-Friendly Interface: Built using Tkinter for ease of use.

Requirements
Python 3.x
Libraries: tkinter, speech_recognition, pyttsx3, datetime, webbrowser, os, random

Installation
Clone the repository:
git clone https://github.com/your-username/voice-assistant-gui.git

Navigate to the project directory:
cd voice-assistant-gui

Install dependencies:
pip install -r requirements.txt

Usage
Run the script:
python main.py

Use voice commands to interact with the assistant. Supported commands include:
"Hello"
"What's the time?"
"Open YouTube"
"Play music"
"Search for [query]"
"Dark mode" / "Light mode"

Folder Structure
main.py: Main script containing the GUI and assistant logic.
C:/music: Default folder for music playback (customizable).

Future Enhancements
Add more commands and functionality.
Improve speech recognition accuracy.
