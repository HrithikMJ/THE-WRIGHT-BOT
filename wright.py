import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()
j=0

def SpeakText(command):


    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while(1):


    try:


        with sr.Microphone() as source2:


            r.adjust_for_ambient_noise(source2, duration=0.2)


            audio2 = r.listen(source2)


            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText)
            if "wright" in MyText or "right" in MyText or "rite" in MyText or "write" in MyText or "rent" in MyText :
                j+=1
                print("\033[1m" + "WRIGHT NUMBER:" + "\033[0m" ,j )

            elif MyText=="exit":
                breaK



    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
