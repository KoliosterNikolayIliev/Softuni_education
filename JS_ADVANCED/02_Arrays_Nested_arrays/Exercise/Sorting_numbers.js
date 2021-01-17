function solve(array) {
    const newList = [];
    let sortedNumbers = array.sort((a, b) => a - b);
    while (sortedNumbers.length > 0) {
        if (sortedNumbers.length == 1) {
            newList.push(sortedNumbers.pop());
            break;
        }
        let min = sortedNumbers.shift()
        let max = sortedNumbers.pop()
        newList.push(min,max)
    }
    return newList
}

console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));