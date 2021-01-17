function rotate(array, n){
    for (let i = 0; i < n; i++) {
        let el = array.pop()
        array.unshift(el)
    }
    return array.join(' ')
}

console.log(rotate(['1',
        '2',
        '3',
        '4'],
    2
));
console.log(rotate(['Banana',
        'Orange',
        'Coconut',
        'Apple'],
    15
));