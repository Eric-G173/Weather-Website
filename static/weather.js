const weatherDescriptions = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",

    45: "Fog",
    48: "Depositing rime fog",

    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",

    56: "Freezing drizzle",
    57: "Freezing drizzle (dense)",

    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",

    66: "Freezing rain",
    67: "Freezing rain (heavy)",

    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",

    77: "Snow grains",

    80: "Rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",

    85: "Snow showers",
    86: "Heavy snow showers",

    95: "Thunderstorm",
    96: "Thunderstorm with hail",
    99: "Severe thunderstorm with hail"
};

let currentScale = "F"; //Default
const dataEl = document.getElementById("weather-data");

const rawTemp = Number(dataEl.dataset.temp);
const rawHigh = Number(dataEl.dataset.high);
const rawLow = Number(dataEl.dataset.low);
const rawFeels = Number(dataEl.dataset.feels);
const conditionCode = Number(document.getElementById("condition").dataset.code);

updateDisplay();



function toF(c) { return c * (9/5) +32; }
function toC(c) { return c }

function convert(c) {
    if (currentScale === "F") return toF(c);
    return toC(c);
}

function updateDisplay() {
    document.getElementById("high").textContent =
        `H: ${Math.round(convert(rawHigh))}°`;

    document.getElementById("low").textContent =
        `L: ${Math.round(convert(rawLow))}°`;

    document.getElementById("feels-like").textContent =
        `Feels like: ${Math.round(convert(rawFeels))}°`;

    document.getElementById("condition").textContent =
    weatherDescriptions[conditionCode] || "Unknown";

    document.getElementById("temp-number").textContent =
    Math.round(convert(rawTemp));

document.querySelector(".temp-scale").textContent =
    `°${currentScale}`;

}

function setScale(scale) {
    currentScale = scale;
    updateDisplay();
}
