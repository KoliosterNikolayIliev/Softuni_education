function solve(commands) {
    let number = 0;
    const numberArray = [];
    for (const command of commands) {
        if (command === 'add') {
            number++;
            numberArray.push(number);
        } else {
            number++;
            numberArray.pop();
        }
    }
    return numberArray.length>0?numberArray.join('\n'):'Empty';
}

// console.log(solve(['add', 'add', 'add', 'add']));
// console.log(solve(['add', 'add', 'remove', 'add', 'add']));
console.log(solve(['remove', 'remove', 'remove']));