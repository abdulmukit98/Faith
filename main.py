import speech_recognition as recognito

listener = recognito.Recognizer()

try:
    with recognito.Microphone() as mic:
        print("listening")
        voice = listener.listen(mic)
        speech = listener.recognize_google(voice)
        print(speech)
        
except:
    pass

