from flask import Flask, render_template, request, session

from API_Function import get_weather, reverse_geocode
from dotenv import load_dotenv
import os
import re

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "test_key") #Test key used as fallback for CI tests
def error_check(city_name):
    if not city_name:
        return "Please enter a city."
    if bool(re.search(r'\d', city_name)):
        return "City cannot contain numbers."
    if len(city_name) > 100:
       return "City name too long."
    return None


@app.route("/")
def home():
    return render_template(
        "index.html",
        error=None
    )


@app.route("/submit", methods=["GET", "POST"])
def submit():
    lat = request.values.get("lat")
    lon = request.values.get("lon")

    if lat and lon:
        city = reverse_geocode(lat, lon)
        if not city:
            return render_template("index.html", error="Unable to determine your city from GPS.")
    else:
        city = request.values.get("city", "")
    session["city"] = city

    error = error_check(city)
    if error:
        return render_template("index.html", error=error)


    data_dict = get_weather(city)
    print("DEBUG city =", city)
    print("DEBUG data_dict =", data_dict)

    return render_template(
        "weather.html",
        city=data_dict["city"],
        country = data_dict["country"],
        temperature=data_dict["tempNow"],
        feels_like = data_dict["feels_like"],
        high = data_dict["temp_max"],
        low = data_dict["temp_min"],
        condition = data_dict["condition"],
    )


if __name__ == "__main__":
    app.run(debug=True)

