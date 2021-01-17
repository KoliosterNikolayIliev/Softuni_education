function order(array) {
    function arrSort(a, b) {
        let result;
        if (a.length === b.length) {
            result = a.localeCompare(b);
        } else {
            result = a.length - b.length;
        }
        return result;
    }

    return array.sort(arrSort).join('\n');

}

console.log(order(['alpha',
        'beta',
        'gamma']

));
console.log(order(['Isacc',
    'Theodor',
    'Jack',
    'Harrison',
    'George']
));
console.log(order(['test',
    'Deny',
    'omen',
    'Default']
));