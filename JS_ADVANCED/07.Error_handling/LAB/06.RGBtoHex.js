function rgbToHexColor(red, green, blue) {
    if (!Number.isInteger(red) || (red < 0) || (red > 255)) {
        return undefined; // Red value is invalid
    }
    if (!Number.isInteger(green) || (green < 0) || (green > 255)) {
        return undefined; // Green value is invalid
    }
    if (!Number.isInteger(blue) || (blue < 0) || (blue > 255)) {
        return undefined; // Blue value is invalid
    }
    return "#" +
        ("0" + red.toString(16).toUpperCase()).slice(-2) +
        ("0" + green.toString(16).toUpperCase()).slice(-2) +
        ("0" + blue.toString(16).toUpperCase()).slice(-2);
}

module.exports = rgbToHexColor;

// console.log(typeof rgbToHexColor(150, 200, 100) == 'string');
// console.log(rgbToHexColor(150, 200, 100) == '#96C864');
// console.log(rgbToHexColor(-50, 200, 100));
// console.log(rgbToHexColor(1000, 200, 100));
// console.log(rgbToHexColor(150, -50, 100));
// console.log(rgbToHexColor(150, 260, 100));
// console.log(rgbToHexColor(150, 200, -100));
// console.log(rgbToHexColor(150, 200, 1000));
// console.log(rgbToHexColor('a', 'b', 'c'));