import requests

def reverse_geocode(lat, lon):
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": lat,
        "lon": lon,
        "zoom": 10,
        "format": "json",
        "addressdetails":1
    }

    data = requests.get(url, params=params, headers={"User-Agent": "CloudySensor"}).json()

    address = data.get("address", {})
    city = (
            address.get("city") or
            address.get("town") or
            address.get("village") or
            address.get("municipality")
    )

    return city

def get_weather(city_name):
    city = city_name
    geo_location = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    response = requests.get(geo_location).json()
    matched_city = response["results"][0]["name"]
    matched_country = response["results"][0]["country"]
    if not response["results"]:
        return {"matched_city": None}
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
    return { # All in Celsius (minus condition)
        "city": matched_city,
        "country": matched_country,
        "tempNow": current["temperature"],              
        "temp_max": daily["temperature_2m_max"][0],     
        "temp_min": daily["temperature_2m_min"][0],     
        "feels_like": current["apparent_temperature"],
        "condition": current["weather_code"]             
    }

