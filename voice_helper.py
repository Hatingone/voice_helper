import pyaudio
import pyttsx3
import speech_recognition as sr
import random
import os
import webbrowser

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say("Здравстуйте я ваш голосовой помощник")
voice.runAndWait()

while True:
    with sr.Microphone(device_index=1) as source:
        print("Скажите что-нибудь...")
        audio = r.listen(source)

    speech = r.recognize_google(audio, language="ru_RU").lower
    print("вы сказали: ", speech)
    
    greetings = ["Привет", "Здравствуйте", "Доброго времени суток", "Хай", "Ку"]
    films = ["Мсители", "Люди в чёрном", "Очень странные дела"]

    if speech.find("привет") >= 0 or speech.find("хай") >=0:
    if greetings in speech:
        voice.say(random.choice(greetings))
        voice.runAndWait()
    if "фильм" in speech:
        random.choice(films)
    elif "открой файл" in speech:
        voice.say("Открываю")
        voice.runAndWait()
        os.startfile("C:/Users/Egork/Desktop/arkanoid.py")
    elif "youtube" in speech:
        webbrowser.open_new("https://www.youtube.com")
    elif "пока" in speech:
        voice.say("до свидания")
        voice.runAndWait()
        break
    else:
        voice.say("я вас не понимаю, повторите пожалуйста")
        voice.runAndWait()
        
