## Jarvis Voice Assistant
A simple Python voice assistant that listens for a wake word and performs basic commands like opening websites.

## Features

Wake word detection: jarvis, hey jarvis, hello jarvis
Speech recognition using Google Speech Recognition
Text-to-speech responses using pyttsx3
Voice commands to open Google, YouTube, Instagram, and Facebook

## Project Structure
main.py
requirements.txt
README.md

# Installation
1. Create a virtual environment (optional)
python -m venv venv


Activate it:

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

2. Install dependencies
pip install -r requirements.txt


Example requirements.txt:

SpeechRecognition
pyttsx3
pyaudio

3. Fix PyAudio installation (Windows)
pip install pipwin
pipwin install pyaudio

# Usage

Run the assistant:

python main.py


Say the wake word “jarvis”, then speak a command.

## Supported Commands
# Command	Action
open google	-> Opens google.com
open youtube ->	Opens youtube.com
open instagram -> Opens instagram.com
open facebook -> Opens facebook.com

# Troubleshooting
Microphone not detected

Ensure your system has a working input device and permissions enabled.

# PyAudio installation errors

Use pipwin on Windows, or install PortAudio on macOS/Linux.

# Speech not understood

Reduce background noise or increase microphone sensitivity.

# License

MIT License