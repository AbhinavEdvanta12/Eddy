import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import math
import operator
import sys

#to print voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#speak function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#wish function
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("please tell me how may i help you")

#take command function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4, phrase_time_limit=7)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        # speak("Say that again please....")
        return "none"
    query = query.lower()
    return query   

#task execution function
def taskExecution():
    wish()
    while True:
        query = takeCommand()

        # logic building for tasks
        if "how are you" in query or "hello eddie how are you" in query:
            speak("I am fine sir, what about you?")

        elif "i am good" in query:
            speak("Thats great sir")

        elif "what is your name" in query:
            speak("my name is eddie")

        elif "who are you" in query:
            speak("i am eddie, i am a virtual voice assistant")

        elif "what can you do for me" in query:
            speak("whatever you want i can do")

        elif "open notepad" in query:
            speak("opening notepad")
            apath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad"
            os.startfile(apath)

        elif "open command prompt" in query:
            speak("opening command prompt")
            os.system("Start cmd")

        elif "play music" in query:
            music_dir = "G:\python\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("Youtube.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "open google" in query:
            speak("What should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open gmail" in query:
            webbrowser.open("gmail.com")

        elif "play song on youtube" in query:
            kit.playonyt("see you again")

        elif "open calculator" in query :
            speak("opening calculator...")
            apath = "G:\eddie\smart-calculator\index.html"
            os.startfile(apath)

        elif "can you do one calculation for me" in query or "can you do an calculation for me" in query or "can you do another calculation for me" in query or "okay so can you do one calculation for me" in query or "okay so can you do an calculation for me" in query:
            speak("I will be honour")       
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Say what you want to calculate")
                print("Listening...")
                r.adjust_for_ambient_noise(source)  #to avoid noise error
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+': operator.add,
                    '-': operator.sub,
                    'x': operator.mul,
                    'divide': operator.truediv,                    
                }[op]

            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            print(eval_binary_expr(*(my_string.split())))        
            speak(eval_binary_expr(*(my_string.split())))        

        elif "you can sleep now" in query or "okay eddie you can sleep now" in query:
            speak("okay sir, i am going to sleep you can call me anytime")
            break 

        elif "goodbye eddie" in query:
            speak("Thanks for using me, have a good day!!!")
            sys.exit()          

        # speak("sir, do you have any other work?")

if __name__ == "__main__":
    # taskExecution()
    while True:
        permission = takeCommand()
        if "wake up" in permission:
            taskExecution()
        elif "goodbye eddie" in permission:
            speak("Thanks for using me, have a good day!!!")
            sys.exit()