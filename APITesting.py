import json
import requests
from flask import render_template 
def Conversion(dataArg, TempType):
    for data in dataArg:
        if data != "condition":
            tempValue = dataArg[data]
            if TempType == "F":
                dataArg[data] = int(tempValue * (9/5) - 459.67)
            elif TempType == "C":
                dataArg[data] = int(tempValue - 273.15)
            elif TempType == "K":
                continue
            else:
                print("An unexpected temperature scale error has occured in APITesting")
    return dataArg


def get_weather(city_name, scale):
    api_key = "dbc6944ae3eb1c455b75a154d922a2f4"
    city = city_name
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") == "404": 
            return None
        main = data["main"]
        weather = data["weather"][0]
        weatherData = {
            "tempNow": main["temp"], 
            "temp_max":main["temp_max"], 
            "temp_min": main["temp_min"], 
            "feels_like":main["feels_like"], 
            "condition": weather["description"]
        } 

    except requests.exceptions.HTTPError:
        print(f"Error, cannot connect to website!")

    except Exception:
        print(f"An unidentified error occured! Ensure city is properly spelled.")
    
    return Conversion(weatherData, scale)


#["main"]["temp_max"] = high
#["main"]["temp_min"] = low
#["main"]["feels_like"] = feels like
#["weather"][0]["description"] = condition