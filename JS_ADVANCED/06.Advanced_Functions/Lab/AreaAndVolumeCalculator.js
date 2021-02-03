function solve(area, vol, input) {
    const figures = JSON.parse(input);
    const output = [];
    for (let figure of figures) {
        let areaFig = Math.abs(area.call(figure));
        let volumeFig = Math.abs(vol.call(figure));
        let result = {};
        result['area'] = areaFig;
        result['volume'] = volumeFig;
        output.push(result);
    }
    return output;
}

function vol() {
    return this.x * this.y * this.z;
}

function area() {
    return this.x * this.y;
}


console.log(solve(area, vol, '[{"x":"1","y":"2","z":"10"},{"x":"7","y":"7","z":"10"},{"x":"5","y":"2","z":"10"}]'));
console.log(solve(area, vol, '[{"x":"10","y":"-22","z":"10"},{"x":"47","y":"7","z":"-5"},{"x":"55","y":"8","z":"0"},{"x":"100","y":"100","z":"100"},{"x":"55","y":"80","z":"250"}]'));
