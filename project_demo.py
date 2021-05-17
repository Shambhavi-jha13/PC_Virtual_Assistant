import speech_recognition as sr

r= sr.Recognizer()

with sr.Microphone() as source:
    print("start saying...!!")
    audio = r.listen(source)
    print("speech done!")
