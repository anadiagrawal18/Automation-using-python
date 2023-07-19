
#the Alex AI is made by Anadi Agrawal. This program executes some specific pre-defined tasks via taking speech input from the user.

import time
import pyttsx3
import datetime
import speech_recognition as sr
import os
import pyautogui
import screen_brightness_control as src





def speak(audio):
    """Speaks what it get in input"""
    a = pyttsx3.init('sapi5') 
    a.say(audio)
    a.runAndWait()


def wishing():
    """WIshes you and ask to what to do"""

    hour = int(datetime.datetime.now().hour)
    crt = datetime.datetime.now().strftime("%H:%M")
    crd =datetime.datetime.now().date()
    crda =datetime.datetime.today().strftime('%A')
    
    if hour>=0 and hour<12:
        
        print(f"Good Morning sir! it's {crt}")
        print(f"Today's Date is {crd}")
        print(f"And Today's Day is {crda}")

        speak(f"Good Morning sir! it's {crt}")
        speak(f"Today's Date is {crd}")
        speak(f"And Today's Day is {crda}")


    elif hour>=12 and hour<18:

        print(f"Good Afternoon sir! it's {crt}")   
        print(f"Today's Date is {crd}")
        print(f"And Today's Day is {crda}")

        speak(f"Good Afternoon sir! it's {crt}")   
        speak(f"Today's Date is {crd}")
        speak(f"And Today's Day is {crda}")

    else:

        print(f"Good Evening sir! it's {crt}") 
        print(f"Today's Date is {crd}")
        print(f"And Today's Day is {crda}")

        speak(f"Good Evening sir! it's {crt}") 
        speak(f"Today's Date is {crd}")
        speak(f"And Today's Day is {crda}")
        

    print("I am Alex here Sir. Please tell me how may I help you!!!")
    speak("I am Alex here Sir. Please tell me how may I help you!!!")  




def telltime():
    """Tell's current time"""
    crt = datetime.datetime.now().strftime("%H:%M")
    print(f"It's {crt}\n")
    speak(f"It's {crt}")




def tdate():
    """Tell's current day and the date"""
    crd =datetime.datetime.now().date()
    crda =datetime.datetime.today().strftime('%A')
    
    print(f"Today's Day is {crda}")
    speak(f"Today's Day is {crda}")
    
    print(f"Today's Date is {crd}\n")
    speak(f"Today's Date is {crd}")




def tkcmd():
    '''takes voice command and return it in string'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        # r.pause_threshold = 1
        speak("Please say the command request")
        audio = r.listen(source)
        

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")
        speak("Say that again please...")
        return "None"

    return query




def searchinit():
    '''used for the same purpose as of tkcmd() but have different linings.'''
    x=1
    nr = sr.Recognizer()
    while x == 1:
        
        with sr.Microphone() as source:
            print("     Listening...")
            nr.adjust_for_ambient_noise(source)
            # r.pause_threshold = 1
            speak("     Please tell what to search or type")
            audio = nr.listen(source)
            

        try:
            print("     Recognizing...")    
            search = nr.recognize_google(audio, language='en-in')
            x=2
            print(f"     User said to search/type for {search}\n")
            
            

        except Exception as e:
            print(e)    
            print("     Say that again please...")
            speak("     Say that again please...")
            x=1 

        
    return search





#main function




if __name__=="__main__":
    wishing()
    while True:
        query = tkcmd().lower()

        if "good morning alex" in query or "good afternoon alex" in query or "good evening alex" in query:
            speak("Greeting from Alex!!!")
            speak("How may i help you!!!")


        if 'tell time' in query or "what's the time" in query:
            telltime()


        if "what's the date" in query or "tell date" in query:
            tdate()
        

        if 'alex sleep' in query:
            x=1
            while x == 1:
                nr = sr.Recognizer()
                with sr.Microphone() as source:
                    print("     Listening...")
                    nr.adjust_for_ambient_noise(source)
                    # r.pause_threshold = 1
                    speak("     Please tell how much time to sleep in seconds")
                    audio = nr.listen(source)
            

                try:
                    print("     Recognizing...")    
                    sleeptime = nr.recognize_google(audio, language='en-in')
                    print(f"     User said to sleep for {sleeptime}\n")
                    x=2
                    speak (f"going to sleep for {sleeptime} seconds")
                    time.sleep(int(sleeptime))
                    speak("Hello sir, i am now up from sleep")

                except Exception as e:
                    print(e)    
                    print("     Say that again please...")
                    speak("     Say that again please...")
                    x=1 




        if 'open youtube in browser' in query:
            # webbrowser.open("youtube.com")
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
            time.sleep(2.5)
            pyautogui.typewrite("youtube.com")
            pyautogui.press("enter")
            
        elif 'open youtube and search' in query:
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
            time.sleep(2.5)
            pyautogui.typewrite("youtube.com")
            pyautogui.press("enter")
            time.sleep(1)
            sear = searchinit().lower()
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("enter")
            pyautogui.typewrite(sear)
            pyautogui.press("enter")
            speak(f"searching in youtube for {sear}")




        if 'open google' in query:
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
            time.sleep(2.5)
            pyautogui.typewrite("google.com")
            pyautogui.press("enter")


        if 'open google classroom' in query:
            os.startfile("D:\\Python Programs\\main progs\\Google Classroom.py")
            print('opening google classroom for you.')
            speak('opening google classroom for you.')


        if 'show desktop' in query or 'minimise all' in query or 'show all' in query:
            pyautogui.keyDown('win')
            pyautogui.press('d')
            pyautogui.keyUp('win')


        if 'open a file' in query:
            searc = searchinit().lower()
            pyautogui.keyDown("win")
            pyautogui.press("s")
            pyautogui.keyUp("win")
            pyautogui.typewrite(searc)
            pyautogui.press("enter")
            speak(f'opening {searc}')


        if 'open browser and search' in query:
            speak("opening firefox web browser")
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
            time.sleep(2.5)
            tksrh = tkcmd().lower()
            pyautogui.typewrite(tksrh)
            pyautogui.press("enter")

        elif  'open web browser' in query:
            speak("opening firefox web browser")
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
            time.sleep(1.5)


        if 'open vs code' in query:
            speak("opening vs code for you.")
            os.startfile("D:\\Microsoft VS Code\\Code.exe")


        if 'open world' in query or 'open word' in query:
            speak("opening word for you.")
            os.startfile("C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.EXE")


        if 'open excel' in query:
            speak("opening powerpoint for you.")
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")


        if 'open excel' in query:
            speak("opening excel for you.")
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")


        if 'show notifications' in query:
            speak("showing notifications now")
            pyautogui.keyDown("win")
            pyautogui.press("n")
            pyautogui.keyUp("win")


        if 'open controls' in query:
            speak("opening basic controls")
            pyautogui.keyDown("win")
            pyautogui.press("a")
            pyautogui.keyUp("win")


        if 'turn night light on' in query:
            speak("turning night light on")
            pyautogui.keyDown("win")
            pyautogui.press("a")
            pyautogui.keyUp("win")
            pyautogui.press("down")
            pyautogui.press("right")
            pyautogui.press("right")
            pyautogui.press("enter")
            pyautogui.press("home")
            pyautogui.keyDown("win")
            pyautogui.press("a")
            pyautogui.keyUp("win")


        if 'turn night light off' in query:
            speak("turning night light off")
            pyautogui.keyDown("win")
            pyautogui.press("a")
            pyautogui.keyUp("win")
            pyautogui.press("down")
            pyautogui.press("right")
            pyautogui.press("right")
            pyautogui.press("enter")
            pyautogui.press("home")
            pyautogui.keyDown("win")
            pyautogui.press("a")
            pyautogui.keyUp("win")


        if 'take screenshot now' in query:
            speak("taking screenshot")
            pyautogui.keyDown("win")
            pyautogui.press("PrtSc")
            pyautogui.keyUp("win")


        if 'show screenshots' in query:
            os.startfile("C:\\Users\\anadi\\Pictures\\Screenshots")


        if 'open task manager' in query:
            os.startfile("C:\\Windows\\system32\\Taskmgr.exe")

        
        if 'open control panel' in query:
            os.startfile("C:\\Users\\anadi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk")


        if 'open command prompt' in query:
            os.startfile("C:\\Windows\\system32\\cmd.exe")


        if 'show hidden icons'in query:
            pyautogui.keyDown("win")
            pyautogui.press("b")
            pyautogui.keyUp("win")
            pyautogui.press('enter')

        
        if 'close hidden icons' in query:
            pyautogui.press('enter')
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")    


        if 'open search' in query:
            speak("Opening windows search") 
            pyautogui.keyDown("win")
            pyautogui.press("s")
            pyautogui.keyUp("win")
            speak("Say what you want to search")
            srh = tkcmd().lower()
            pyautogui.typewrite(srh)
            pyautogui.press("enter")


        if 'switch tabs' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")


        if 'switch 2 tabs' in query or 'switch to tabs' in query or 'switch two tabs' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")


        if 'open notepad' in query:
            os.startfile("C:\\Windows\\system32\\notepad.exe")


        if 'open settings' in query:
            speak("Opening settings")
            pyautogui.keyDown("win")
            pyautogui.press("i")
            pyautogui.keyUp("win")


        if 'open file explorer' in query:
            speak("opening file explorer")
            pyautogui.keyDown("win")
            pyautogui.press("e")
            pyautogui.keyUp("win")


        if 'open camera' in query:
            speak("opening camera")
            pyautogui.keyDown("win")
            pyautogui.press("s")
            pyautogui.keyUp("win")
            pyautogui.typewrite('camera')
            pyautogui.press("enter")


        if 'open photos' in query:
            speak("opening photos app")
            pyautogui.keyDown("win")
            pyautogui.press("s")
            pyautogui.keyUp("win")
            pyautogui.typewrite('photos')
            pyautogui.press("enter")

        
        if 'open office' in query:
            speak("opening office")
            pyautogui.keyDown("win")
            pyautogui.press("s")
            pyautogui.keyUp("win")
            pyautogui.typewrite('office')
            pyautogui.press("enter")


        if 'open calculator' in query:
            speak("opening calculator")
            pyautogui.keyDown("fn")
            pyautogui.press("f12")
            pyautogui.keyUp("fn")


        if 'play music' in query:
            speak('playing music now')
            pyautogui.hotkey('win', 's')
            pyautogui.typewrite('Media Player')
            time.sleep(3)
            pyautogui.press('space')


        if 'open microsoft store' in query:
            speak("opening microsoft store")
            pyautogui.keyDown("win")
            pyautogui.press("s")
            pyautogui.keyUp("win")
            pyautogui.typewrite('microsoft store')
            pyautogui.press("enter")


        if 'open clock' in query:
            speak("opening clock")
            pyautogui.keyDown("win")
            pyautogui.press("s")
            pyautogui.keyUp("win")
            pyautogui.typewrite('clock')
            pyautogui.press("enter")


        if 'open mail' in query:
            speak("opening mail")
            pyautogui.keyDown("win")
            pyautogui.press("s")
            pyautogui.keyUp("win")
            pyautogui.typewrite('mail')
            pyautogui.press("enter")

        
        if 'open calender' in query:
            speak("opening calender")
            pyautogui.keyDown("win")
            pyautogui.press("s")
            pyautogui.keyUp("win")
            pyautogui.typewrite('calender')
            pyautogui.press("enter")


        if 'open weather' in query:
            speak("opening weather app for you")
            pyautogui.keyDown("win")
            pyautogui.press("s")
            pyautogui.keyUp("win")
            pyautogui.typewrite('weather')
            pyautogui.press("enter")


        if 'open game bar' in query:
            speak("opening game bar")
            pyautogui.keyDown("win")
            pyautogui.press("g")
            pyautogui.keyUp("win")


        if 'open adobe pdf' in query:
            speak("opening adobe acrobat dc")
            os.startfile("C:\\Program Files\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe")


        if 'close current window' in query:
            speak("Closing Current window")
            pyautogui.keyDown("alt")
            pyautogui.press("f4")
            pyautogui.keyUp("alt")

        
        if 'press tab' in query:
            pyautogui.press("tab")


        if 'press enter' in query:
            pyautogui.press("enter")


        if 'press backspace' in query:
            pyautogui.press("backspace")


        if 'press space' in query:
            pyautogui.press("space")


        if 'type' in query:
            w=searchinit().lower()
            pyautogui.typewrite(w)


        if 'press escape' in query:
            pyautogui.press("esc")


        if 'sleep the laptop' in query:
            pyautogui.press('win')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('right')
            pyautogui.press('enter')
            pyautogui.press('enter')


        if 'lock the laptop' in query:
            pyautogui.press('win')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.press('down')
            pyautogui.press('enter')
            

        if 'backspace' in query:
            pyautogui.press('backspace')


        if 'page down' in query:
            pyautogui.press('pgdn')


        if 'page up' in query:
            pyautogui.press('pgup')

        
        if 'show system info' in query:
            cmd = 'systeminfo'
            os.system(cmd)


        if 'check for windows update' in query:
            pyautogui.hotkey('win', 'i')
            time.sleep(1)
            pyautogui.press('down',11)
            pyautogui.press('enter')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('checking for windows updates')
            speak('checking for windows updates')
            

        
        if 'increase volume' in query:
            pyautogui.press('volumeup')


        if 'decrease volume' in query:
            pyautogui.press('volumedown')

        
        if 'mute now' in query or 'mute volume' in query or 'unmute' in query:
            pyautogui.press('volumemute')


        if 'current brightness' in query:
            a = src.get_brightness()
            print(f'current brightness is {a}')
            speak(f'current brightness is {a}')


        if 'set brightness' in query:
            a = src.get_brightness()
            print(f'current brightness is {a}')
            speak(f'current brightness is {a}')
            set = int(searchinit())
            if set == 100 or set == 'hundred' in query:
                src.set_brightness(100)
            else:
                src.set_brightness(set)


        if 'exit program' in query:

            print("Exiting Program. Hope you have a nice day sir.")
            speak("Exiting Program. Hope you have a nice day sir.")
            print("I would like to thank you for using me and also thank you my creater Mr. Anadi Agrawal for creating me.")
            speak("I would like to thank you for using me and also thank you my creater Mr. Anadi Agrawal for creating me.")
            exit()


#End of program