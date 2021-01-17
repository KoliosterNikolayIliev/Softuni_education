function findNeighbours(nestedArray) {
    let pairs = 0;
    for (let i = 0; i < nestedArray.length - 1; i++) {
        for (let j = 0; j < nestedArray[i].length; j++) {
            if (nestedArray[i][j] === nestedArray[i + 1][j] && i < nestedArray.length) {
                pairs += 1;
            }
            if (nestedArray[i][j] === nestedArray[i][j + 1]) {
                pairs += 1;
            }
            if (nestedArray[i + 1][j] === nestedArray[i + 1][j + 1]) {
                pairs += 1;
            }
        }
    }


    console.log(pairs);
}

findNeighbours([['2', '3', '4', '7', '0'],
    ['4', '0', '5', '3', '4'],
    ['2', '3', '5', '4', '2'],
    ['9', '8', '7', '5', '4']]
);
findNeighbours([['test', 'yes', 'yo', 'ho'],
    ['well', 'done', 'yo', '6'],
    ['not', 'done', 'yet', '5']]
);

findNeighbours([[2, 2, 2], [2, 2, 2], [2, 2, 2]]);
