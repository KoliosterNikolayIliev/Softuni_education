function townToJSON(table) {
    let matrix = [];
    let jsonObj = [];
    for (const el of table) {
        let elPure = el.slice(2, el.length - 2);
        matrix.push(elPure.split(' | '));
    }
    let names = matrix.shift();
    for (const item of matrix) {
        let obj = {};
        obj[names[0]] = item[0];
        obj[names[1]] = Math.round((Number(item[1]) + Number.EPSILON) * 100) / 100;
        obj[names[2]] = Math.round((Number(item[2]) + Number.EPSILON) * 100) / 100;
        jsonObj.push(obj);
    }
    return JSON.stringify(jsonObj);

}


console.log(townToJSON(['| Town | Latitude | Longitude |',
    '| Sofia | 42.696552 | 23.32601 |',
    '| Beijing | 39.913818 | 116.363625 |']
));

console.log(townToJSON(['| Town | Latitude | Longitude |',
    '| Veliko Turnovo | 43.0757 | 25.6172 |',
    '| Monatevideo | 34.50 | 56.11 |']
));