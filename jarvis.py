import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import pywhatkit as kit
import sys

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning,Hello Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, Hello Sir")
    elif hour >= 18 and hour < 20:
        speak("Good Evening, Hello Sir")
    else:
        speak("Hello Sir")
    speak("Jarvis at your service. Please tell me how can I help you")


def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(
            audio, language='en-in')  #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please..."
              )  #Say that again will be printed in case of improper voice
        speak("Say that again please...")
        return "None"  #None string will be returned
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who are you' in query:
            speak(
                "my name is jarvis sir, I am a desktop assitant assigned for you"
            )

        elif 'who made you' in query:
            speak("abhishek soni")

        elif 'play song on youtube' in query:
            kit.playonyt("see you again")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("sir,what should i search")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'go to training' in query:
            webbrowser.open("trainings.internshala.com")

        elif 'open makaut portal' in query:
            webbrowser.open("makaut1.ucanapply.com")

        elif 'open command promt' in query:
            os.system("start cmd")

        elif 'open notepad' in query:
            codePath = "C:\\Windows\\system32\\notepad.exe"
            speak("Sure Sir")
            os.startfile(codePath)

        elif 'open onscreen keyboard' in query:
            codePath = "C:\\Windows\\system32\\osk.exe"
            speak("Sure Sir")
            os.startfile(codePath)

        elif 'send message' in query:
            kit.sendwhatmsg("+918789246965","hello Sir, I am jarvis how may I help you", 3, 40)
            speak("message sent sir")

        elif "jarvis take rest" in query:
            speak("okay, have a good day sir")
            sys.exit()
