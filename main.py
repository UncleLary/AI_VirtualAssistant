import webbrowser, os, time, pyautogui
from pynput.keyboard import Controller
from dotenv import load_dotenv
from localMachineFunctions import speak, speakTime, speakDate, takeCommand, assistantInit, goodbyeFunction, openNotebook, openDiscord, \
    openCalculator, openDownloads, openCMD, openTeams, openScreenshots, takeScreenshot, cpuUsage, batteryPercentage, \
    batteryWarning, openTaskManager, openExpenses, openChrome, openBrave, openTor
from onlineFunctions import getRandomJoke, findMyIP, playOnYoutube, searchOnGoogle, searchWikipedia,chatWithAssistant, getTrendingMovies
import weatherFunctions
load_dotenv()
assistandName = os.getenv("ASSISTANT_NAME")

if __name__ == '__main__':
    assistantInit()
    batteryWarning()
    exit_keywords = ["end", "exit", "goodbye", "stop", "offline", "good night", "bye"]
    exit_flag = False
    command = takeCommand()

    while (exit_flag == False):
        command = takeCommand()
        if "chat".lower() in command.lower():
            speak("I'm waiting for prompt now")
            prompt = takeCommand()
            print(f"{assistandName}: " + chatWithAssistant(prompt))
            speak(chatWithAssistant(prompt))

        if (any(keyword.lower() in command.lower() for keyword in exit_keywords)):
            exit_flag = True
        else:
            sites = [["youtube", "https://youtube.com"],
                     ["wikipedia", "https://wikipedia.com"],
                     ["gmail", "https://mail.google.com/mail/u/2/#inbox"],
                     ["google", "https://google.com"],
                     ["facebook", "https://facebook.com"],
                     ["instagram", "https://instagram.com"],
                     ["chatgpt", "https://chat.openai.com/"],
                     ["translator", "https://translate.google.com/?sl=en&tl=pl&op=translate&hl=pl"]]

            for site in sites:
                if f"open {site[0]}".lower() in command.lower():
                    speak(f"Opening {site[0]} sir")
                    webbrowser.open(site[1])

            if "time".lower() in command.lower():
                speakTime()

            if "date".lower() in command.lower():
                speakDate()

            if "open Notepad".lower() in command.lower() or "open Notebook".lower() in command.lower():
                openNotebook()

            if "open Expenses".lower() in command.lower():
                openExpenses()

            if "open Spotify".lower() in command.lower():
                os.system(r'start "" "Spotify"')
                speak("Spotify opened!")

                # text_to_write = 'Piękny Świat'
                # # text_to_write = 'angry playlist'
                # # speak("What music would you like?")
                # # text_to_write = takeCommand()
                # # print(f"User chose: '{text_to_write}' song")
                #
                # time.sleep(5)
                # pyautogui.hotkey('ctrl', 'l')
                # time.sleep(1)
                # # pyautogui.typewrite(text_to_write, interval = 0.1   )
                # Controller().type(text_to_write)    #allows using Polish letters like ę, ł, ć etc.
                #
                # for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
                #     time.sleep(2)
                #     pyautogui.press(key)

            if "open Downloads".lower() in command.lower():
                openDownloads()

            if "open Calculator".lower() in command.lower():
                openCalculator()

            if "open Discord".lower() in command.lower():
                openDiscord()

            if "open Chrome".lower() in command.lower():
                openChrome()

            if "open Brave".lower() in command.lower():
                openBrave()

            if any(keyword.lower() in command.lower() for keyword in ["open Tor", "open The Onion Router", "open Onion Router", "open Onion"]):
                openTor()

            if any(keyword.lower() in command.lower() for keyword in ["open team", "open teams", "open microsoft teams", "open microsoft team"]):
                openTeams()

            if any(keyword.lower() in command.lower() for keyword in ["open cmd", "open command prompt"]):
                if ("as admin" or "as administrator") in command.lower():
                    openCMD(as_admin=True)
                else:
                    openCMD()

            if 'ip address'.lower() in command.lower():
                findMyIP()

            if 'joke' in command.lower():
                getRandomJoke()

            if any(keyword.lower() in command.lower() for keyword in ["search on Wikipedia", "search Wikipedia"]):
                searchWikipedia()

            if any(keyword.lower() in command.lower() for keyword in ["search on Google", "search in Google", "search Google"]):
                searchOnGoogle()

            if any(keyword.lower() in command.lower() for keyword in ["search on Youtube", "play on Youtube"]):
                playOnYoutube()

            if 'take screenshot' in command.lower():
                takeScreenshot()

            if any(keyword.lower() in command.lower() for keyword in ["open Screenshot", "open Screenshots"]):
                openScreenshots()

            if 'open Task Manager'.lower() in command.lower():
                openTaskManager()

            if 'CPU'.lower() in command.lower():
                cpuUsage()

            if 'battery'.lower() in command.lower():
                batteryPercentage()

            if "movies".lower() in command.lower():
                getTrendingMovies()

            if "weather".lower() in command.lower():
                print(f"{assistandName}: What city do you want to serch for?")
                app = weatherFunctions.WeatherApp()
                app.run()
                # speak("What city do you want to serch for?")
                # command = takeCommand()
                # searchFunction()
                # getTodaysWeather("New York")

    goodbyeFunction()