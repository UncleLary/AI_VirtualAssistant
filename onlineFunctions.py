import textwrap, requests, wikipedia, inflect, os, cohere
import pywhatkit as kit
from localMachineFunctions import speak, takeCommand, workingOnItMessage
from dotenv import load_dotenv

load_dotenv()
assistandName = os.getenv("ASSISTANT_NAME")
cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(cohere_api_key)
tmbd_api_key = os.getenv("TMDB_API_KEY")


def getRandomJoke():
    #warning! Dad jokes!!
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    speak(res["joke"])
    print(f"{assistandName}: " + res["joke"])

def findMyIP():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    ip_address = ip_address["ip"]
    p = inflect.engine()
    address_parts = ip_address.split('.')
    converted_parts = [p.number_to_words(part) for part in address_parts]
    converted_ip = ' '.join(converted_parts)
    speak(f'Your IP Address is {converted_ip}.\n For your convenience, I am printing it on the screen sir.')
    print(f'{assistandName}: Your IP Address is {ip_address}')

def playOnYoutube():
    searching = True
    while searching:
        speak('What do you want me to search on Youtube?')
        videoTitle = takeCommand().lower()
        speak(workingOnItMessage())
        print(f"{assistandName} User wanted to search: {videoTitle} on Youtube")

        try:
            kit.playonyt(videoTitle)
            searching = False
        except Exception as e:
            print(f"An error occurred: {e}")
            speak("Sorry, I encountered an error while searching on YouTube. Please try again.")

def searchOnGoogle():
    searching = True
    while searching:
        speak(f'{assistandName}: What do you want me to search on Google?')
        topic = takeCommand().lower()
        speak(workingOnItMessage())
        print(f"User wanted to search: {topic} on Google")
        try:
            kit.search(topic)
            searching = False
        except Exception as e:
            print(f"{assistandName}: An error occurred: {str(e)}")
            speak("Sorry, I encountered an error while searching on Google. Please try again.")


def searchWikipedia():
    searching = True
    while searching:
        speak("What should I search in Wikipedia?")
        topic = takeCommand()
        print(f"{assistandName}: User wanted to search: {topic} in Wikipedia")
        speak(workingOnItMessage())

        if topic.strip():  # Assuming an empty string is an invalid input
            try:
                results = wikipedia.summary(topic, auto_suggest=False)
                print(results)
                searching = False
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)
                speak("Sorry, I couldn't find a specific page for that topic. Please try again.")
            except wikipedia.exceptions.PageError:
                print(f"{assistandName}: Page for '{topic}' does not exist on Wikipedia. Please try another topic.")
                speak(f"Page for '{topic}' does not exist on Wikipedia. Please try another topic.")
        else:
            print("Invalid input. Please provide a valid topic.")
            speak("Sorry, that's not a valid topic. Please try again.")

def chatWithAssistant(prompt):
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens = 350,
        temperature = 1)
    return response.generations[0].text


def getTrendingMovies():
    speak(workingOnItMessage())
    howManyResults = 5
    trending_movies = []
    res = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={tmbd_api_key}").json()
    results = res["results"]

    for r in results[:howManyResults]:
        title = r.get("original_title", "N/A")
        release_date = r.get("release_date", "N/A")
        vote_average = r.get("vote_average", "N/A")
        overview = r.get("overview", "N/A")

        terminal_width = 120
        wrapped_overview = textwrap.fill(overview, width=terminal_width)

        trending_movies.append(title)
        print(f"{assistandName}: Title: '{title}' \t Released: {release_date} \t Average Rating: {vote_average} \nOverview: {wrapped_overview}\n")

    speak(f"Here is top {howManyResults} trending movies: {trending_movies}")


