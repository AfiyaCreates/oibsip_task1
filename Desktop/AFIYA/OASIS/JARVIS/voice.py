import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Initialize the text-to-speech 
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)

# Function to speak out the given text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user based on the current time    
def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 
    else:
        speak("Good Evening!")        
    speak('i am mikasa!, please tell me how may i help you?')  

# Function to take user's command through the microphone    
def takecommand():
# it takes microphone input from the user and returns string output 
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  
        r.pause_thershold = 1
        r.energy_threshold=300
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said:", query)
    except Exception as e:
        # print(e)
        print("say that agian please...")
        return"None"
    return query  
if __name__=="__main__":
    wishme()
    while True:
        # Take user's command
        query = takecommand().lower()
        #logic for executing tasks based on query
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("according to wikipedia...")
            print(results)
            speak(results)
        elif "open google" in query:
            speak("opening google...")
            webbrowser.open("google.com")
        elif "open youtube" in query:
            speak("opening youtube...")
            webbrowser.open("youtube.com") 
        elif "hello mikasa i am" in query:
            query= query.replace("hello mikasa i am","")  
            speak("hello" + query + "how may i help you?")
        elif "the time " in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is...")
            speak(time)   
        elif "play music" in query:
            music= 'C:\\Users\\MAHAD\\Music'  
            songs = os.listdir(music) 
            # print(songs)
            speak("playing music...")
            os.startfile(os.path.join(music,songs[2]))
        elif "quit" in query:
            speak("signing off ...thank you!")
            exit()   
         
            




    



      
