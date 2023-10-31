#AI_VirtualAssistant
This project is my attempt to create my own Jarvis from IronMan series. With power of Python libraries and APIs, I'm developing my virtual assitant powered by AI.

Right now, you can chat with him, he is capable of opening some programs, searching Wikipedia/Youtube/Google, play a song on Spotify, display weather conditions, get some trending movies, warn you about low battery% and give notification to plug/unplug the charger, tell you some joke, tell you your IP address, take a screenshoot, tell you current CPU usage, tell you current time and/or date, get your command(recognize speech). 
I want to enrich the assistant with reasoning from the text and making decisions on that basis. Furthermore, I want it to be able to create and manage notifications/reminders/calendar by itself. I also plan to create a GUI. Feel free to follow changes! : )

Project is not finished yet, but I'm proud of current effect and I decided to share it on my Github, to maybe inspire someone.

If you want to download and run it on your own, you need to create .env file(template provided in repo), and put there paths to applications and API keys.

Used API: COHERE(LLM Model), OPENWEATHER(Weather info&icons), TMDB(TheMovieDataBase - getting info about trendind movies). Also I use request to site with jokes: https://icanhazdadjoke.com/, but it doesnt need private key. 
