import datetime
import pyttsx3


engine = pyttsx3.init()     # Engine property modifications
engine.setProperty('rate', 235)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):        # Function to Speak
    engine.say(text)
    engine.runAndWait()
    
def time():     # Function to "Speak" Time
    currTime = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current Time is: ")
    speak(currTime)


