import requests
import win32com.client
import json

# Get the city name from user input
city = input("Enter the name of the city: ")

# Construct the URL for weather data using the WeatherAPI
url = f"https://api.weatherapi.com/v1/current.json?key=1332be73b6934f0cb0e170359242802&q={city}"

# Make an HTTP GET request to fetch weather data
r = requests.get(url)

# Parse the JSON response into a dictionary
wdic = json.loads(r.text)

# Extract the current temperature in Celsius from the dictionary
w = wdic["current"]["temp_c"]

# Initialize the text-to-speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Speak the current weather information
speaker.Speak(f"The current weather in {city} is {w:.1f} degrees Celsius.")
