import speech_recognition as sr

r = sr.Recognizer()
audio= 'record.wav'
with sr.AudioFile(audio) as source:
    print("Speak Anything :")
    audio = r.record(source)
    print('Done')
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")