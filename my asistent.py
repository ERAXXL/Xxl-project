import speech_recognition as sr
import pyttsx3


#Бот ответчик
# создаем объекты для распознавания речи и синтеза речи
r = sr.Recognizer()
engine = pyttsx3.init()

# устанавливаем голос и скорость синтеза
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

# определяем функцию для распознавания и ответа на голосовой ввод
def recognize_speech():
    with sr.Microphone() as source:
        print("Говорите...")
        audio = r.listen(source)
        print(audio)
        try:
            text = r.recognize_google(audio, language="ru-RU")
            print(f"Вы сказали: {text}")
            engine.say("Вы сказали " + text)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Речь не распознана")
            engine.say("Речь не распознана")
            engine.runAndWait()

        except sr.RequestError as e:
            print(f"Ошибка сервиса распознавания речи: {e}")
            engine.say("Ошибка сервиса распознавания речи")
            engine.runAndWait()


# вызываем функцию для распознавания речи

while True:
    with sr.Microphone() as source:
            print("Скажите секретный слова...")
            audio = r.listen(source)
            text = r.recognize_google(audio, language="ru-RU")
            engine.runAndWait()
            print(text)
    if text == "ноутбук":
        recognize_speech()
    if text == "айфон":
        break 
    else:
        continue 
