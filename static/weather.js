const dataEl = document.getElementById("weather-data");

const rawTemp = Number(dataEl.dataset.temp);
const rawHigh = Number(dataEl.dataset.high);
const rawLow = Number(dataEl.dataset.low);
const rawFeels = Number(dataEl.dataset.feels);

updateDisplay();

let defaultScale= "F"; // Will be default for website

function toF(c) { return c * (9/5) +32; }
function toC(c) { return c }

function convert(c) {
    if (currentScale === "F") return toF(c);
    return toC(c);
}

function updateDisplay() {
    document.getElementById("temp").textContent =
        `${convert(rawTemp).toFixed(1)}°${currentScale}`;

    document.getElementById("high").textContent =
        `H: ${convert(rawHigh).toFixed(1)}°`;

    document.getElementById("low").textContent =
        `L: ${convert(rawLow).toFixed(1)}°`;

    document.getElementById("feels-like").textContent =
        `Feels like: ${convert(rawFeels).toFixed(1)}°`;
}

function setScale(scale) {
    currentScale = scale;
    updateDisplay();
}
