import datetime
import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()     # Engine property modifications
engine.setProperty('rate', 235)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):        # Function to Speak
    engine.say(text)
    engine.runAndWait()
engine = pyttsx3.init()     # Engine property modifications
engine.setProperty('rate', 235)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):        # Function to Speak
    engine.say(text)
    engine.runAndWait()


def greet():        # Function to "Speak" a greeting pertaining to the current time
    hour = datetime.datetime.now().hour
    if hour <= 6 and hour < 12:
        speak("Good Morning to you!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon to you!")

    elif hour >= 18 and hour < 24:
        speak("Good Evening to you!")

    else:
        speak("Good Night to you!")
