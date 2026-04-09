import requests



def get_weather(city_name):
    city = city_name
    geo_location = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    response = requests.get(geo_location).json()
    if response.get("cod") == "404": 
        return None
    lat = response["results"][0]["latitude"]
    lon = response["results"][0]["longitude"]

    weather_url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={lat}&longitude={lon}"
    f"&current=temperature,apparent_temperature,weather_code"
    f"&daily=temperature_2m_max,temperature_2m_min"
    )

    weather_response = requests.get(weather_url).json()
    current = weather_response["current"]
    daily = weather_response["daily"]
    print(current["temperature"],)
    return { # All in Celsius (minus condition)
        "tempNow": current["temperature"],              
        "temp_max": daily["temperature_2m_max"][0],     
        "temp_min": daily["temperature_2m_min"][0],     
        "feels_like": current["apparent_temperature"],
        "condition": current["weather_code"]             
    }

