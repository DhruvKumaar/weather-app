# Weather App

## Overview

This is a simple desktop GUI application built using Python and Tkinter. It allows users to check the current weather of any city by fetching real-time data from the OpenWeatherMap API.

## Features

- Displays current temperature in Celsius.
- Shows weather condition description.
- Displays humidity percentage.
- Handles errors for invalid city names or network issues.
- Clean and easy-to-use graphical interface.

## Technologies Used

- **Programming Language**: Python
- **GUI Library**: Tkinter
- **API Service**: [OpenWeatherMap](https://openweathermap.org)

## How It Works

1. The user enters the name of a city in the input field.
2. When the button is clicked, the app sends a request to OpenWeatherMap using the city name.
3. The app processes the returned JSON data and extracts temperature, condition, and humidity.
4. The information is displayed on the GUI in a formatted layout.

## Setup Instructions

1. Download or clone the project files.
2. Install the required Python library:

```bash
pip install requests
```

3. Open the script and replace the `API_KEY` variable with your own key from [OpenWeatherMap](https://openweathermap.org/api).
4. Run the Python file:

```bash
python weather_app.py
```

## Notes

- A working internet connection is required to fetch the weather data.
- You can register for a free API key at: [https://openweathermap.org/api](https://openweathermap.org/api)
