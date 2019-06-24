import speech_recognition as sr

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print('Say Something:')
        audio = r.listen(source, phrase_time_limit=5)
    try:
        text = r.recognize_google(audio, language='bn-BD')

        print(text)
        print(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
