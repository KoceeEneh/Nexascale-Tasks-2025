import requests
import os


API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


def get_weather(city):

    # api request parameter

    params = {"q": city.strip(), "appid": API_KEY, "units": "metric"}

    # send request to API
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # check if request was successful
    if response.status_code == 200:

        # extracting details
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        # displaying the details
        print(f"weather in {city}: ")
        print("Temperature: " + str(temperature) + "°C")
        print("Condition: " + condition)
        print("Humidity: " + str(humidity) + "%")

    else:
        print(f"could not find weather for {city} . please enter a valid city name. ")


# user input
city_name = input("Enter city name: ")
get_weather(city_name)
