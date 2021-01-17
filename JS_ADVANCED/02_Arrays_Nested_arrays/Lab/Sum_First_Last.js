function calcFirsLast(numberStrings) {
    let a = Number(numberStrings.shift());
    let b = Number(numberStrings.pop());
    let sum = a + b;
    return console.log(sum);
}

calcFirsLast(['20', '30', '40']);
calcFirsLast(['5', '10']);