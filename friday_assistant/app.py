import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice', voice[1].id)

def speak(audio) :
    print('F.I:' + audio)
    friday.say(audio)
    friday.runAndWait()

def time() : 
    Time = datetime.datetime.now().strftime("%I: %M: %p")
    print(datetime.datetime.now().hour)

    # speak(Time)
def welcome():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning")
    elif hour < 18:
        speak("Good afternoon")
    else: 
        speak("Good evening")
    speak("How can i help you")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language = "en")
        print("Admin :" + query)
    except sr.UnknownValueError:
        print("Try again")
        query = str(input("Your order is :"))
    return query

if __name__  == "__main__":
    welcome()
    while 1:
        query = command().lower();
        if "google" in query:
            speak("what should i search in google?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} in google")
        if "youtube" in query:
            speak("what should i search in youtube?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} in youtube")


    