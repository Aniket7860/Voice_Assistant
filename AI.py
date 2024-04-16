import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import pyjokes
import os
import playsound
from gtts import gTTS
import pywhatkit





engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 
  

    speak("I am Voice assistant developed by Aniket")
        

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
        speak("Say that again please...") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
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

        elif 'open youtube' in query or 'youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query or 'google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query or 'stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query or 'music' in query:
            speak("opening music")
            music_dir ='D:\music\ringtone.mp3'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("opening code")
            codePath = "C:\\Users\\Aniket\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that you are fine")
               
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Aniket")

        elif "will you be my girlfriend" in query or "will you be my boyfriend" in query:  
            speak("I'm not sure about, may be you should give me some time")
        
        elif "i love you" in query:
            speak("It's hard to understand")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'hai' in query:
            speak("hello")

        elif 'who are you' in query:   
            speak("You don't know me,i am your best friend") 
        
        elif 'yes' in query:
            speak("I am so happy because you know me")
            
        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("maavie","") 
            query = query.replace("google search","") 
            query = query.replace("google","") 
            speak("this is what i found on the web!") 
        
            try:
                pywhatkit.search(query)
                result = googleScrap.summary(query,3) 
                speak(result)  
                
            except:
                speak("No speakable Data available")
                
                
        elif 'ok' in query:
            speak("Anything else")
            speak("if you wanna leave than say to me exit....")

        elif 'email to abhishek' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "gulloo06@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email") 
                
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
