// function types(...args) {
//     let dataTypes = {};
//     for (let arg of args) {
//         if (dataTypes[typeof arg]) {
//             dataTypes[typeof arg].push(arg);
//         } else {
//             dataTypes[typeof arg] = [];
//             dataTypes[typeof arg].push(arg);
//         }
//     }
//     let result2 = '';
//     let result = '';
//     let sortable = [];
//     for (const [key, values] of Object.entries(dataTypes)) {
//         for (let value of values) {
//             result += (`${key}: ${value}\n`);
//         }
//         sortable.push([key, values.length]);
//
//     }
//     sortable.sort(function (a, b) {
//         return b[1] - a[1];
//     });
//     for (let i = 0; i < sortable.length; i++) {
//         result2 += (`${sortable[i][0]} = ${sortable[i][1]}\n`);
//     }
//
//     console.log(result + result2);
// }
//
// // types('cat', 42, function () {
// //     console.log('Hello world!');
// // });
//
// types(42, 'cat', 15, 'kitten', 'tomcat')
let expectedOutput = [
    'number: 42',
    'string: cat',
    'number: 15',
    'string: kitten',
    'string: tomcat',
    'string = 3',
    'number = 2'
];

// function argInfo(...input) {
//     let info = new Map();
//
//     input.forEach(x => {
//         let type = typeof x;
//
//         if (!info.has(type)) {
//             info.set(type, 0);
//         }
//
//         info.set(type, info.get(type) + 1);
//         console.log(`${type}: ${x}`);
//     });
//
//     [...info].sort(([aType, aCount], [bType, bCount]) => bCount - aCount)
//         .forEach(([type, count]) => {
//             console.log(`${type} = ${count}`);
//         });
// }
//
// argInfo(42, 'cat', 15, 'kitten', 'tomcat')

function argumentInfo(...arguments) {
    let typeCounts = {};
    for(let arg of arguments){
        console.log(`${typeof(arg)}: ${arg}`);
        if(! typeCounts[typeof(arg)]){
            typeCounts[typeof(arg)] = 1;
        } else {
            typeCounts[typeof(arg)]++;
        }
    }

    Object.keys(typeCounts).sort((a, b) => typeCounts[b] - typeCounts[a]).forEach(k => console.log(`${k} = ${typeCounts[k]}`))
}
argumentInfo(42, 'cat', 15, 'kitten', 'tomcat')