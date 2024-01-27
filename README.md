# Python Virtual Assistant

This Python script serves as a virtual assistant that responds to voice commands to open various software applications. It utilizes speech recognition, text-to-speech, and system commands to provide a hands-free interaction experience.

## Features

- **Voice Recognition:** The assistant uses the `speech_recognition` library to recognize voice commands.
- **Text-to-Speech:** The `pyttsx3` library is employed for converting text to speech, making the assistant responsive.
- **Software Launch:** The assistant can open specific software applications based on the recognized commands.
- **Gender Selection:** Users can choose between a male and a female voice for the assistant.

## Setup

1. **Install the required libraries:**

   ```bash
   pip install pyttsx3
   pip install SpeechRecognition
Ensure a working microphone is connected to your system.

Run the script:

```bash
python virtual_assistant.py
```
Follow the on-screen instructions to select the assistant's gender and command the opening of software applications.

Supported Software
Microsoft Word
Microsoft PowerPoint
Microsoft Excel
Google Chrome
VLC Player
Notepad
Audacity
Usage
Start the script and choose the desired assistant gender.

Command the assistant to open specific software by stating the software's name.

The assistant will respond with a confirmation and launch the requested application.

To exit the assistant, say "exit."

Example
  ```bash
  # Start the script
  python virtual_assistant.py

  # Assistant prompts for gender selection

  # Command the assistant to open Microsoft Word
  # Assistant responds and opens Microsoft Word

  # Command the assistant to exit
  # Assistant exits with a farewell message
  ```
## Notes
Make sure to adjust microphone settings if voice commands are not recognized accurately.
Supported on Windows operating systems.

## License
This project is licensed under the MIT License.
