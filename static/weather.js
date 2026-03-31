let rawTemp = null;
let rawHigh = null;
let rawLow = null;
let rawFeels = null;

let defaultScale= "F"; // Will be default for website

function toF(c) { return c * (9/5) +32; }
function toC(c) { return c }
function toK(c) { return c + 273.15; }

function convert(c) {
    if (currentScale === "F") return toF(c);
    if (currentScale === "K") return toC(c);
    return toK(c);
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
