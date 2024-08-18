import pyttsx3 as p
import speech_recognition as sr
engine=p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate', 180)
engine.say("hello im jatin chauhan")
engine.runAndWait() 

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("hello sir i am your assitant")
r=sr.Recognizer()
with sr.Microphone as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio=r.listen(source)
    infor=r.recognize_google(audio)

assit=infow()  
assit.get.info(infor)  
    

if "what" and "about" and "you" in text:
    speak("i am good tell about you")

speak("what can i do for you")

