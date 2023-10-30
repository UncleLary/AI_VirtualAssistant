from dotenv import load_dotenv
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap
import os


class WeatherApp:
    def __init__(self):
        load_dotenv()
        self.weather_api_key = os.getenv("OPENWEATHER_API")

        self.root = ttkbootstrap.Window(themename="morph")
        self.root.title("Weather App")
        self.root.geometry("850x600")

        self.city_entry = ttkbootstrap.Entry(self.root, font="Helvetica, 18")
        self.city_entry.pack(pady=10)

        self.search_button = ttkbootstrap.Button(self.root, text="Search", command=self.search_function,
                                                 bootstyle="warning")
        self.search_button.pack(pady=10)

        self.location_label = tk.Label(self.root, font="Helvetica, 25")
        self.location_label.pack(pady=20)

        self.icon_label = tk.Label(self.root)
        self.icon_label.pack()

        self.temperature_label = tk.Label(self.root, font="Helvetica, 20")
        self.temperature_label.pack()

        self.feels_like_label = tk.Label(self.root, font="Helvetica, 20")
        self.feels_like_label.pack()

        self.description_label = tk.Label(self.root, font="Helvetica, 20")
        self.description_label.pack()

    def get_todays_weather(self, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}"
        res = requests.get(url)

        if res.status_code == 404:
            messagebox.showerror("Error 404", "City not found :/")
            return None

        weather = res.json()
        icon_id = weather['weather'][0]['icon']
        temperature = weather['main']['temp'] - 273.15
        feels_like = weather['main']['feels_like'] - 273.15
        description = weather['weather'][0]['description']
        city_name = weather['name']
        country = weather['sys']['country']

        icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
        return (icon_url, temperature, feels_like, description, city_name, country)

    def update_gui(self, result):
        if result is None:
            return

        icon_url, temperature, feels_like, description, city, country = result
        image = Image.open(requests.get(icon_url, stream=True).raw)
        icon = ImageTk.PhotoImage(image)
        self.icon_label.configure(image=icon)
        self.icon_label.image = icon

        self.temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
        self.feels_like_label.configure(text=f"Feels like: {feels_like:.2f}°C")
        self.description_label.configure(text=f"Description: {description}")

    def search_function(self):
        city = self.city_entry.get()
        result = self.get_todays_weather(city)
        self.update_gui(result)

    def run(self):
        self.root.mainloop()