function findBiggest(matrix) {
    function combineMax(arr) {
        const combinedArray = [];
        for (const array of arr) {
            let subRes = array.sort((a, b) => a - b);
            subRes = subRes[subRes.length - 1];
            combinedArray.push(subRes);
        }
        return combinedArray;
    }

    const flat_array = combineMax(matrix);
    let result = flat_array.sort((a, b) => a - b);
    result = result[result.length - 1];
    return result;
}

console.log(findBiggest([[20, 50, 10],
    [8, 33, 145]]
));
console.log(findBiggest([[3, 5, 7, 12],
    [-1, 4, 33, 2],
    [8, 3, 0, 4]]
));