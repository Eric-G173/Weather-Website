from flask import Flask, render_template, request, session, redirect

import APITesting
from errorValidation import errorCheck
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def home():
    return render_template(
        "index.html",
        error=None
    )



@app.route("/submit", methods=["POST"])
def submit():
    city = request.form.get("city")
    session["city"] = city

    error = errorCheck(city)
    if error:
        return render_template("index.html", error=error)

    dataDict = APITesting.get_weather(city)
    return render_template(
        "weather.html",
        city=city,
        temperature=dataDict["tempNow"],
        feels_like = dataDict["feels_like"],
        high = dataDict["temp_max"],
        low = dataDict["temp_min"],
        condition = dataDict["condition"],
    )


if __name__ == "__main__":
    app.run(debug=True)

