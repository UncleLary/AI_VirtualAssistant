import pyttsx3 as tts
import speech_recognition as sr
import datetime, os, random, pyautogui, psutil
from dotenv import load_dotenv
from plyer import notification


load_dotenv()
assistandName = os.getenv("ASSISTANT_NAME")

paths = {
    "Notepad": os.getenv("Notepad"),
    "Downloads": os.getenv("Downloads"),
    "Discord": os.getenv("Discord"),
    "Teams": os.getenv("Teams"),
    "Calculator": os.getenv("Calculator"),
    "Screenshots": os.getenv("Screenshots"),
    "Expenses": os.getenv("Expenses"),
    "Chrome": os.getenv("Chrome"),
    "Brave": os.getenv("Brave") ,
    "Tor": os.getenv("Tor")
}

def workingOnItMessage():
    openingTaskTexts = [
        "Cool, I'm on it.",
        "Okay, I'm working on it.",
        "Just a second.",
        "On it.",
        "Working on it.",
        "As you wish",
        "I shall attend to it immediately.",
        "Will do",
        "At your service.",
        "Task initiated.",
        "Engaging protocols, sir.",
        "Processing your command."
    ]
    return random.choice(openingTaskTexts)

def speak(message):
    engine = tts.init()
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)  # 0-Polish Woman, 1- Eng Woman, 2 - Eng Male
    engine.say(message)
    engine.runAndWait()

def speakTime():
    currentTime = datetime.datetime.now().strftime("%H:%M")
    speak(currentTime)

def speakDate():
    currentDate = datetime.date.today()
    currentDate.strftime("%d/%B/%Y")
    print(currentDate.strftime("%d/%m/%Y"))
    speak(currentDate)

def takeCommand():
    while(1):
        recognizer = sr.Recognizer()
        speak("I'm lisstening!")
        print(f"{assistandName}: I'm lisstening!")
        try:
            with sr.Microphone() as source:
                recognizer.pause_threshold = 0.5  #by defualt: 0.8s - it defines duration of silence considered as the end of speaking
                recognizer.adjust_for_ambient_noise(source, 0.5)
                command = recognizer.listen(source)
                query = recognizer.recognize_google(command, language="en-pl")
                # query = recognizer.recognize_google(command, language="pl-en")
                print(f"User said: {query}")
                return query
        except Exception as execption:
            print(f"Sorry, there was an error: {execption}")
            speak("Sorry, there was an error")


def assistantInit():
    hour = datetime.datetime.now().strftime("%H")
    hour = int(hour)

    if (hour >= 4) and (hour < 12):
        speak(f"Good Morning")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon")
    elif (hour >= 16) and (hour < 22):
        speak(f"Good Evening")
    else:
        speak("Good Evening, it's getting late.")

    speak(f"How may I assist you today?")

def goodbyeFunction():
    hour = datetime.datetime.now().strftime("%H")
    hour = int(hour)
    if (hour >= 4) and (hour < 21):
        speak("Goodbye, I'm going offline now")
    else:
        speak("Goodnight, I wish you a peacefull rest. Going offline now")


# def createEvent():
#     speak("What's event title?")
#     event = takeCommand()


# def remindMe():
#     speak("About what event should I remind you?")
#     event = takeCommand()
#     speak("In what time should I remind you?")
#     eventTime = takeCommand()
#     currentTime = datetime.datetime.now().strftime("%H:%M")


def openNotebook():
    app_name = "Notepad"
    app_path = paths[app_name]
    os.system(r'start "" "{}"'.format(app_path))
    speak("{} opened!".format(app_name))


def openDownloads():
    app_name = "Downloads"
    app_path = paths[app_name]
    os.system(r'start "" "{}"'.format(app_path))
    speak("{} opened!".format(app_name))

def openDiscord():
    app_name = "Discord"
    app_path = paths[app_name]
    os.system(r'start "" "{}"'.format(app_path))
    speak("{} opened!".format(app_name))

def openTeams():
    app_name = "Teams"
    app_path = paths[app_name]
    os.system(r'start "" "{}"'.format(app_path))
    speak("{} opened!".format(app_name))

def openCMD(as_admin=False):
    if as_admin:
        os.system("start runas /user:Administrator cmd")
        speak("Administrator Command Prompt opened!")
    else:
        os.system("start cmd")
        speak("Command Prompt opened!")

def openCalculator():
    app_name = "Calculator"
    app_path = paths[app_name]
    os.system(r'start "" "{}"'.format(app_path))
    speak("{} opened!".format(app_name))

def openScreenshots():
    app_name = "Screenshots"
    app_path = paths[app_name]
    os.system(r'start "" "{}"'.format(app_path))
    speak("{} opened!".format(app_name))

def openExpenses():
    app_name = "Expenses"
    app_path = paths[app_name]
    os.system(r'start excel "{}"'.format(app_path))
    speak("{} opened!".format(app_name))

def openChrome():
    app_name = "Chrome"
    app_path = paths[app_name]
    os.system(r'start "" "{}"'.format(app_path))
    speak("{} opened!".format(app_name))

def openBrave():
    app_name = "Brave"
    app_path = paths[app_name]
    os.system(r'start "" "{}"'.format(app_path))
    speak("{} opened!".format(app_name))

def openTor():
    app_name = "Tor"
    app_path = paths[app_name]
    os.system(r'start "" "{}"'.format(app_path))
    speak("{} opened!".format(app_name))

def takeScreenshot():
    speak(workingOnItMessage())
    pyautogui.hotkey('win', 'prntscrn')

def openTaskManager():
    speak(workingOnItMessage())
    pyautogui.hotkey('ctrl', 'shift', 'esc')

def cpuUsage():
    cpuUsagePer = psutil.cpu_percent()
    print("CPU usage is at: " + str(cpuUsagePer) + "%")
    speak("CPU usage is at: " + str(cpuUsagePer) + "%")

def batteryPercentage():
    battery = psutil.sensors_battery()
    speak("Battery is at: " + str(battery.percent) + "%")
    print("Battery is at: " + str(battery.percent) + "%")

def batteryWarning():
    battery = psutil.sensors_battery()
    batteryPercent = battery.percent
    batteryPercentStr = str(battery.percent)


    if(battery.power_plugged == True):
        print("Battery charger is plugged.")

        if (battery.percent == 100):
            notification_title = "Battery is fully charged!"
            notification_message = f"Battery is at {batteryPercentStr}%! Unplug the charger please."
            notification.notify(title=notification_title, message=notification_message, timeout=10)  # Display the notification for 10 seconds
            speak("Battery is fully charged! Unplug the charger please.")

        elif (batteryPercent >= 95):
            notification_title = "Battery is almost fully charged!"
            notification_message = f"Battery is at {batteryPercentStr}%! I suggest unplugging the charger.."
            notification.notify(title=notification_title, message=notification_message, timeout=10)  # Display the notification for 10 seconds
            speak("Battery is: " + batteryPercentStr + "%! I suggest unplugging the charger.")


    if (battery.power_plugged == False):
        print("Battery charger is not plugged.")

        print("Battery is at: " + batteryPercentStr + "%")

        if (battery.percent < 15):
            speak("Warning: Battery is at critical: " + batteryPercentStr + "%!  Charge it imidiately please!")
        elif (battery.percent < 20):
            speak("Warning: Battery is only " + batteryPercentStr + "%! I strongly suggest charging.")
        elif(battery.percent < 50):
            speak("Battery is at: " + batteryPercentStr + "%! I suggest charging.")


