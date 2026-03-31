let rawTemp = null;
let rawHigh = null;
let rawLow = null;
let rawFeels = null;

let defaultScale= "F"; // Will be default for website

function toF(k) { return (k - 273.15) * 9/5 + 32; }
function toC(k) { return k - 273.15; }
function toK(k) { return k; }

function convert(k) {
    if (currentScale === "F") return toF(k);
    if (currentScale === "C") return toC(k);
    return toK(k);
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
