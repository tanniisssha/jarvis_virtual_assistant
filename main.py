import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pyjokes 
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
        print("Good Afternoon")
    else:
        speak("Good Evening!")  
        print("Good Evening!")
    speak("I am Jarvis mam. Please tell me how may I help you")       
    print("I am Jarvis mam. Please tell me how may I help you")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play music' in query:
            music_dir ='C:\\Users\\ADMIN\\Music\\music.mp3' 
            songs = os.listdir(music_dir)
            print(songs)
            x = len(songs)
            y = random.randint(0,x)    
            os.startfile(os.path.join(music_dir, songs[y]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mam , the time is {strTime}")
            print(f"Mam , the time is {strTime}")
        elif 'open code' in query:
            codePath = 'C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        elif 'joke' in query:
          speak(pyjokes.get_joke())
          print(pyjokes.get_joke())
        elif 'your name' in query:
            speak('My name is JARVIS')
            print('My name is JARVIS')
        elif 'who made you' in query:
            speak('I was created by my AI master in 2023')
            print('I was created by my AI master in 2023')
        elif 'stands for' in query:
            speak('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')
            print('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')
        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)
            speak("Hello mam, I have switched my voice. How is it?")
        elif "remember that" in query:
            speak("What should I remember")
            data = takeCommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))
        elif "good" in query:
            speak("Glad to hear that mam!!")
            print("Glad to hear that mam!!")
        elif "how are you" in query:
            speak("I'm fine mam, What about you?")
            print("I'm fine mam, What about you?")
        elif "quit" in query:
            quit()