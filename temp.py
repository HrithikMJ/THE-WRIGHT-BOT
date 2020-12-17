import speech_recognition as sr

r = sr.Recognizer()
main_text = []
wright_count = 0

with sr.Microphone() as source:

    def recorder():
        print("Speak: ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text, type(text))
            main_text.append(text)
            for i in main_text:
                if "right" in i:
                    wright_count += 1
            print(wright_count)
        except:
            print("Try Again")
            print(wright_count)
            recorder()
    recorder()
