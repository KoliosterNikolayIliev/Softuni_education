function minTwoNumbers(numbers) {
    let sortedNumbers = numbers.sort((a, b) => a - b);
    return console.log(sortedNumbers[0], sortedNumbers[1]);
}

minTwoNumbers([30, 15, 50, 5]);
minTwoNumbers([3, 0, 10, 4, 7, 3]);