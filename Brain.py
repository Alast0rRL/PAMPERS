import speech_recognition as sr
import pyttsx3
import serial
import time
import sys
import re

# Инициализация порта и библиотек для речи
ser = serial.Serial('COM3', 9600)
start = pyttsx3.init()

# Флаг для определения режима прослушивания
listening_mode = False

# Функция для произношения текста и вывода в консоль
def say(text):
    print(text)
    start.say(text)
    start.runAndWait()

# Функция для прослушивания команд
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Настройка параметров для прослушивания
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            # Распознавание команды с использованием Google Speech Recognition
            task = r.recognize_google(audio, language="ru-RU").lower()
            return task
        except sr.UnknownValueError:
            return None

# Функция для обработки команд
def process_command(command):
    if "включи свет" in command and "свет" in command:
        say("Включаю светодиод")
        ser.write(b'1')
    elif "выключи свет" in command:
        say("Выключаю светодиод")
        ser.write(b'0')
    elif "двигатель" in command:
        ser.write(b'3')
        ser.write(b'0')
        say("Кручу")
    elif "поверни на" in command and "градусов" in command:
        print("Не удалось извлечь угол из команды")
        #match = re.search(r'(?:угол|градусов)\s*(\d+)', command)
        #angle = int(match.group(1))
        #return angle
        #angle_value = extract_angle(command)
        #print(f"Извлеченный угол: {angle_value} градусов")

        ##
        print()
    elif "стоп" in command:
        say("Стоп")
        global listening_mode
        listening_mode = False

# Основная функция программы
def main():
    global listening_mode

    while True:
        # Если не в режиме прослушивания, ждем фразу "Окей памперс"
        if not listening_mode:
            command = listen()

            if command and ("о'кей пампер" in command or "о'кей pampers" in command):
                say("Памперс слушает")
                listening_mode = True
            
            if command and ("о'кей тостер" in command):
                say("Памперс слушает")
                listening_mode = True

        # В режиме прослушивания обрабатываем команды
        else:
            command = listen()

            if command:
                process_command(command)


# Запуск программы
say('Активация прошла успешно')
if __name__ == "__main__":
    main()