import speech_recognition as sr
import pyttsx3


#Бот ответчик
# создаем объекты для распознавания речи и синтеза речи
r = sr.Recognizer()
engine = pyttsx3.init()

# устанавливаем голос и скорость синтеза
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)

# определяем функцию для распознавания и ответа на голосовой ввод
while True:
    print("Напеши слова")
    text = input()
    print(f"Вы сказали: {text}")
    engine.say(text)
    engine.runAndWait()

