# oibsip_task1

# Voice Assistant - Mikasa

## Overview
This Python script is a basic voice assistant named Mikasa. It utilizes the `pyttsx3` library for text-to-speech, `speech_recognition` for recognizing user commands through the microphone, and various functionalities to perform tasks based on user input.

## Features
- Greets the user based on the current time of the day.
- Listens to user commands through the microphone.
- Performs tasks such as:
  - Searching on Wikipedia.
  - Opening Google or YouTube in a web browser.
  - Responding to user introductions.
  - Providing the current time.
  - Playing music from a specified directory.
  - Quitting the voice assistant.

## Requirements
- Python 3.x
- `pyttsx3` library
- `speech_recognition` library
- `wikipedia` library
- Internet connection for Wikipedia searches
- Default web browser for opening Google and YouTube
- Music files in the specified directory for playing music

## Installation
1. Install required Python libraries:
   ```bash
   pip install pyttsx3
   pip install SpeechRecognition
   pip install wikipedia
   ```

## Usage
1. Run the script:
   ```bash
   python voice.py
   ```
2. The voice assistant will greet you and wait for your commands.
3. Speak your command, and Mikasa will respond accordingly.

## Supported Commands
- Wikipedia searches
- Opening Google or YouTube
- User introductions
- Getting the current time
- Playing music
- Quitting the voice assistant

## Note
- Adjust the `music` variable in the script to point to the directory where your music files are stored.
- Ensure a stable internet connection for Wikipedia searches.

Feel free to customize and expand the functionalities as needed. Enjoy interacting with Mikasa!
```
