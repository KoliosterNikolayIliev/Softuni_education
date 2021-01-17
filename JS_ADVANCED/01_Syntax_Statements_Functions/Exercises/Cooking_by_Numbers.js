function cook(...array) {
    let inputNumber = Number(array.shift());
    for (const argument of array) {
        switch (argument) {

            case 'chop':
                inputNumber = inputNumber / 2;
                console.log(inputNumber);
                break;
            case 'dice':
                inputNumber = Math.sqrt(inputNumber);
                console.log(inputNumber);
                break;
            case 'spice':
                inputNumber += 1;
                console.log(inputNumber);
                break;
            case 'bake':
                inputNumber = inputNumber * 3;
                console.log(inputNumber);
                break;
            case 'fillet':
                inputNumber -= 0.2 * inputNumber;
                console.log(inputNumber);
                break;
        }
    }
}

cook('32', 'chop', 'chop', 'chop', 'chop', 'chop')
cook('9', 'dice', 'spice', 'chop', 'bake', 'fillet')