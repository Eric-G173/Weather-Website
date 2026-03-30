from flask import Flask, render_template, request, session, redirect

import APITesting
from errorValidation import errorCheck

app = Flask(__name__)
app.secret_key = "superweatherfatapp"


# ---------------------------
# HOME PAGE
# ---------------------------
@app.route("/")
def home():
    return render_template(
        "index.html",
        error=None
    )


# ---------------------------
# SUBMIT FORM → SECOND PAGE
# ---------------------------
@app.route("/submit", methods=["POST"])
def submit():
    city = request.form.get("city")
    session["city"] = city

    error = errorCheck(city)
    if error:
        return render_template("index.html", error=error)

    scale = session.get("scale", "F")
    dataDict = APITesting.get_weather(city, scale)
    return render_template(
        "weather.html",
        city=city,
        temperature=dataDict["tempNow"],
        feels_like = dataDict["feels_like"],
        high = dataDict["temp_max"],
        low = dataDict["temp_min"],
        condition = dataDict["condition"],
        tempScale=scale
    )


# ---------------------------
# TEMP SCALE PARTIAL UPDATE
# ---------------------------
@app.route("/tempScale", methods=["POST"])
def tempScale():
    print("FORM:", request.form)

    scale = request.form.get("tempScale")  # Gets from post value

    session["scale"] = scale  #Stores it after
    scale = session.get("scale", "F")
    city = session.get("city")
    dataDict = {
        "tempNow": None,
        "feels_like": None,
        "temp_max": None,
        "temp_min": None,
        "condition": None
    }
    if city:
        dataDict = APITesting.get_weather(city, scale)
    return render_template(
        "partials/temperature.html",
         city=city,
        temperature=dataDict["tempNow"],
        feels_like = dataDict["feels_like"],
        high = dataDict["temp_max"],
        low = dataDict["temp_min"],
        condition = dataDict["condition"],
        tempScale=scale,
        error = None
    )

if __name__ == "__main__":
    app.run(debug=True)

