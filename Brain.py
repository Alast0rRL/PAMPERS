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
#Функция "Слушай"
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
            task = say("Не слышу")
        return task
#Функция "Делй"
def request(task):
    if "включи свет" in task:
        say("Включаю светодиод")
        ser.write(b'1')
    elif "выключи свет" in task:
        say("Выключаю светодиод")
        ser.write(b'0')
    elif "серво" in task:
        say("Кручу")  
        ser.write(b'2')
    elif "стоп" in task:
        sys.exit()
        
    
#Стартуем
try:
    while True:
    	request(listen())
except:
	say('Выключаюсь') 