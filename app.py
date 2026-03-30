from flask import Flask, render_template, request, session, redirect
from livereload import Server # For VSC testing only, remove if moved to web host

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
    session["scale"] = request.form.get("tempScale")
    city = session.get("city")
    scale = session.get("scale", "F")

    temperature = None
    if city:
        temperature = APITesting.get_weather(city, scale)

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


# ---------------------------
# LIVERELOAD SERVER
# ---------------------------
# For VSC testing only, remove if moved to web host
if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.watch('static/*.css')
    server.watch('templates/*.html')
    server.watch('templates/**/*.html')
    server.serve(port=5000, debug=True)