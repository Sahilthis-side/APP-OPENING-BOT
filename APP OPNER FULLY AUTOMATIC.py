import pyttsx3
import os
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')

engine.say("""WELCOME SIR !
YOUR VIRTUAL ASSISTANT IS READY TO HELP YOU.
PLEASE SAY MALE FOR MALE ASSISTANT
PLEASE SAY FEMALE FOR FEMALE ASSISTANT""")
engine.runAndWait()

print("WELCOME SIR !")
print("YOUR VIRTUAL ASSISTANT IS READY TO HELP YOU.")
print("PLEASE SAY MALE FOR MALE ASSISTANT")
print("PLEASE SAY FEMALE FOR FEMALE ASSISTANT")


with mic as source:
    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source)

audio = r.recognize_google(audio)


if audio == "Female".lower():
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)

engine.say("PLEASE TELL ME THE NAME OF THE SOFTWARE YOU WANT TO OPEN")
engine.runAndWait()
engine.say("""WE HAVE THE FOLLOWING LIST OF SOFTWARE :
    SAY MS WORD FOR > MICROSOFT WORD
    SAY MS POWERPOINT FOR > MICROSOFT POWERPOINT
    SAY MS EXCEL For > MICROSOFT EXCEL
    SAY GOOGLE CHROME FOR > GOOGLE CHROME
    SAY VLC PLAYER FOR > VLC PLAYER
    SAY NOTEPAD FOR > NOTEPAD
    "SAY AUDACITY FOR > AUDACITY"
    SAY EXIT TO STOP ME """)

engine.runAndWait()


while True:
    engine.say("PLEASE TELL ME THE NAME OF THE SOFTWARE YOU WANT TO OPEN")
    engine.runAndWait()
    print("PLEASE TELL ME THE NAME OF THE SOFTWARE YOU WANT TO OPEN")
    print("WE HAVE THE FOLLOWING LIST OF SOFTWARE : ")
    print("SAY MS WORD FOR > MICROSOFT WORD")
    print("SAY MS POWERPOINT FOR > MICROSOFT POWERPOINT")
    print("SAY MS EXCEL For > MICROSOFT EXCEL")
    print("SAY GOOGLE CHROME FOR > GOOGLE CHROME")
    print("SAY VLC PLAYER FOR > VLC PLAYER")
    print("SAY NOTEPAD FOR > NOTEPAD")
    print("SAY AUDACITY FOR > AUDACITY")
    print("SAY EXIT TO STOP ME ")


    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

    audio = r.recognize_google(audio)

    if audio.lower() == "ms word":
        engine.say("Starting Microsoft Word")
        engine.runAndWait()
        os.system("start winword")
        continue

    elif audio.lower() == "ms powerpoint":
        engine.say("Starting Microsoft Powerpoint")
        engine.runAndWait()
        os.system("start powerpnt")
        pass

    elif audio.lower() == "ms excel":
        engine.say("Starting Microsoft Excel")
        engine.runAndWait()
        os.system("start excel")
        pass

    elif audio.lower() == "google chrome":
        engine.say("Starting Google Chrome")
        engine.runAndWait()
        os.system("start chrome")
        pass

    elif audio.lower() == "vlc player":
        engine.say("Starting VLC Player")
        engine.runAndWait()
        os.system("start vlc")
        pass

    elif audio.lower() == "notepad":
        engine.say("Starting Notepad")
        engine.runAndWait()
        os.system("start notepad")
        pass

    elif audio.lower() == "exit":
        engine.say("EXITING ! THANK YOU FOR CHOOSING ME, HAVE A NICE DAY !")
        engine.runAndWait()
        exit()

    else:
        engine.say("I CAN'T RECOGNIZE YOU SIR ! PLEASE TRY AGAIN.")
        engine.runAndWait()
