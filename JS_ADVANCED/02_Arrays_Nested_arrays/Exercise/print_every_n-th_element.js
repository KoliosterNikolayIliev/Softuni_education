// function solve(array, number) {
//     return array.filter(function (el) {return array.indexOf(el) % number !== 1;});
// }

function solve(array, number) {
    const filtered = [];
    for (let i = 0; i < array.length; i++) {
        if (i%number==0){
            filtered.push(array[i])
        }
    }
    return filtered
}


console.log(solve([5, 20, 31, 4, 20], 2));


console.log(solve(['dsa',
        'asd',
        'test',
        'tset'],
    2
));

console.log(solve(['1',
        '2',
        '3',
        '4',
        '5'],
    6
));