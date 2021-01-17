function solve(array) {
    const newArr = [];
    while (array.length > 0) {
        let toPushNext = array.shift();
        if (newArr[newArr.length - 1] <= toPushNext || newArr.length==0) {
            newArr.push(toPushNext);
        }
    }
    return newArr;
}

console.log(solve([1, 3, 8, 4, 10, 12, 3, 2, 24]));

console.log(solve([1,
    2,
    3,
    4]
));
console.log(solve([100]));