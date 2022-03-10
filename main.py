import speech_recognition as sr
import pyttsx3

Faith = pyttsx3.init()
Faith.say("Welcome to Bliss")
Faith.runAndWait()

listener = sr.Recognizer()

try:
    with sr.Microphone() as mic:
        listener.adjust_for_ambient_noise(mic)

        print("listening")
        voice = listener.listen(mic)
        print("complete")
        speech = listener.recognize_google(voice)
        speech = speech.lower()
        print(speech)

except:
    pass

