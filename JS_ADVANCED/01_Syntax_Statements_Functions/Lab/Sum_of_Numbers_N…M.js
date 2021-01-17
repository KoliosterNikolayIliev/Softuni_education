function sumOfNumbers(first, second) {
    let numOne = Number(first);
    let numTwo = Number(second);
    let sum = 0
    for (let i = numOne; i <= numTwo; i++) {
        sum += i;
    }
    return sum
}

console.log(sumOfNumbers('1', '5'))
console.log(sumOfNumbers('-8', '20'))
