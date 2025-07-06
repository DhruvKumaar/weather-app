import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "dfb1a673a073ab8c1196916c39beb207"

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]

        temperature_label.config(text=f"🌡 Temperature: {temp} °C")
        description_label.config(text=f"☁️ Condition: {desc}")
        humidity_label.config(text=f"💧 Humidity: {humidity}%")
        result_frame.pack(pady=10)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve data.\n{e}")

root = tk.Tk()
root.title("Weather App")
root.geometry("420x400")
root.configure(bg="#e6f2ff")

title = tk.Label(root, text="🌤️ Weather App", font=("Segoe UI", 20, "bold"), bg="#e6f2ff", fg="#333")
title.pack(pady=20)

input_frame = tk.Frame(root, bg="#e6f2ff")
input_frame.pack(pady=10)

city_label = tk.Label(input_frame, text="Enter City Name:", font=("Segoe UI", 12), bg="#e6f2ff")
city_label.pack(side="left", padx=5)

city_entry = tk.Entry(input_frame, font=("Segoe UI", 12), width=25)
city_entry.pack(side="left", padx=5)

search_button = tk.Button(root, text="Get Weather", font=("Segoe UI", 12), bg="#007bff", fg="white", width=20, command=get_weather)
search_button.pack(pady=10)

result_frame = tk.Frame(root, bg="white", padx=15, pady=15, bd=1, relief=tk.RIDGE)

temperature_label = tk.Label(result_frame, text="", font=("Segoe UI", 13), bg="white", fg="#333")
temperature_label.pack(pady=5)

description_label = tk.Label(result_frame, text="", font=("Segoe UI", 13), bg="white", fg="#333")
description_label.pack(pady=5)

humidity_label = tk.Label(result_frame, text="", font=("Segoe UI", 13), bg="white", fg="#333")
humidity_label.pack(pady=5)

root.mainloop()