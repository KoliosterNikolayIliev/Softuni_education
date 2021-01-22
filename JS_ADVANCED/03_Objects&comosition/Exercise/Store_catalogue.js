function catalogueSort(data) {
    let rawData = {};
    let keys = [];
    let alphaKeys = {}
    for (const element of data) {
        const converted = element.split(' : ');
        converted[1] = Number(converted[1]);
        converted[0] = converted[0];
        rawData[converted[0]] = converted[1];
        keys.push(converted[0]);
    }
    keys.sort((a, b) => a.localeCompare(b));
    let result = '';
    let alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
    while (alphabet.length>0){
        let alpha = alphabet.shift()
        if (keys[0] === undefined){break}
        let k = keys[0][0]
        while (alpha === k){
            if (alphaKeys[alpha] === undefined) {
                alphaKeys[alpha]=[]
            }
            if (keys.length === 0 || keys[0][0] !== alpha){break}
            let value = keys.shift()
            let keyValue = []
            keyValue.push(value)
            keyValue.push(rawData[value])
            alphaKeys[alpha].push(keyValue)
        }
    }
    for (const [key, value] of Object.entries(alphaKeys)) {
        result+=key+'\n'
        for (const item of value) {
            result+=` ${item[0]}: ${item[1]}\n`
        }
    }

    return result;
}

console.log(catalogueSort(['Appricot : 20.4', 'Fridge : 1500',
    'TV : 1499',
    'Deodorant : 10',
    'Boiler : 300',
    'Apple : 1.25',
    'Anti-Bug Spray : 15',
    'T-Shirt : 10']
));

console.log(catalogueSort(['Banana : 2', 'Rubic\'s Cube : 5',
    'Raspberry P : 4999',
    'Rolex : 100000',
    'Rollon : 10',
    'Rali Car : 2000000',
    'Pesho : 0.000001',
    'Barrel : 10']
));