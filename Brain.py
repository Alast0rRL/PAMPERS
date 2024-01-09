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
#Функция Слушай_памперса
def listen_pamp():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
        try:
            task_pamp = r.recognize_google(audio, language="ru-RU").lower()
            print(task_pamp)
            request_pamp()
        except:
            task_pamp = listen_pamp()
        return task_pamp
#Функция "Если памперс"
def request_pamp(task_pamp):
    if("о'кей пампер"in task_pamp)and("о'кей pampers"in task_pamp):   
        say('Памперс слушает request')
        listen()
    else:
        say("ошибка")
#Функция слушай
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
            request()
        except:
            task = listen()
        return task
#Функция делай
def request(task):
    if("включи свет" in task)and("свет"in task):
        say("Включаю светодиод")
        ser.write(b'1')
    elif "выключи свет" in task:
        say("Выключаю светодиод")
        ser.write(b'0')
    elif("двигатель" in task):
        say("Кручу")  
        ser.write(b'2')
    elif "о'кей pampers" in task:
        say("Памперс слушает")
    elif "стоп" in task:
        sys.exit()
        
    
#Стартуем
while True:
        request_pamp(listen_pamp())
