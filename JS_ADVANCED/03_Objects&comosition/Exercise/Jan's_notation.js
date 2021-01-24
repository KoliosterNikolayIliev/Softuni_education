function solve(data) {
    const tempArr = [];
    while (data.length > 0) {
        let element = data.shift();
        if (typeof element === 'string') {
            if (tempArr.length<2){return 'Error: not enough operands!'}
            let numOne = tempArr.pop();
            let numTwo = tempArr.pop();
            let result;
            if (element === '+') {
                result = numOne + numTwo;
                data.unshift(result);
            }
            if (element === '-') {
                result = numTwo - numOne;
                data.unshift(result);
            }
            if (element === '*') {
                result = numOne * numTwo;
                data.unshift(result);
            }
            if (element === '/') {
                result = numTwo / numOne;
                data.unshift(result);
            }

        }
        if (typeof element!=='string'){
            tempArr.push(element);
        }

    }
    if (tempArr.length>1){return 'Error: too many operands!'}
    return tempArr[0]
}

// console.log(solve([3, 4,2,'+','/']));
// console.log(solve([5, 3, 4, '*', '-']));
// console.log(solve([7, 33, 8, '-']));
// console.log(solve([15, '/']));