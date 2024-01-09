import speech_recognition as sr
import pyttsx3
import os
import serial
import time
import sys

ser = serial.Serial('COM3', 9600)
start = pyttsx3.init()

#Функция "скажи"
def say(a):
    print(a)
    start.say(a)
    start.runAndWait()
#Функция "Слушай о'кей памперса"
def listen_pampers():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
        try:
            pampers_words = r.recognize_google(audio, language="ru-RU").lower()
            print(pampers_words)
        except:
            pampers_words = listen_pampers()
        return pampers_words
#Функция проверки о'кей памперса
def request_pamp(pampers_words):
    if("о'кей памперс","о'кей pampers" in pampers_words):
        request(listen)
    else:
        request_pamp(listen_pampers())
#Функция Слушай
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        say('Памперс слушает')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
        try:
            task = r.recognize_google(audio, language="ru-RU").lower()
            print(task)
        except:
            task = listen()
        return task
#Функция "Делй"
def request(task):
    if("включи свет" in task)and("свет"):
        say("Включаю светодиод")
        ser.write(b'1')
    elif "выключи свет" in task:
        say("Выключаю светодиод")
        ser.write(b'0')
    elif "pampers серво" in task:
        say("Кручу")  
        ser.write(b'2')
    elif "о'кей pampers" in task:
        say("Памперс слушает")
    elif "стоп" in task:
        sys.exit()

        
    
#Стартуем
while True:
        request_pamp(listen_pampers())
