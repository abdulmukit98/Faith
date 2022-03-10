import speech_recognition as recognito
import pyttsx3

Faith = pyttsx3.init()
Faith.say("Welcome to Bliss")
Faith.runAndWait()

listener = recognito.Recognizer()
try:
    with recognito.Microphone() as mic:
        print("listening")
        voice = listener.listen(mic)
        speech = listener.recognize_google(voice)
        speech = speech.lower()
        print(speech)

except:
    pass

