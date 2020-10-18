import speech_recognition as sr
import docx as do

doc=do.Document()
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    print('Done')
    try:
        text = r.recognize_google(audio)
        doc.add_paragraph(text)
        doc.save('finally.docx')
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")
