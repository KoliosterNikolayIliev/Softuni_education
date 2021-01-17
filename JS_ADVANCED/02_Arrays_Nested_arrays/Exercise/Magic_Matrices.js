function findIfMagical(matrix) {
    let sumRows = '';
    let sumCols = '';
    for (let i = 0; i < matrix.length; i++) {
        let rowSum = 0;
        let colSum = 0;
        for (let j = 0; j < matrix[i].length; j++) {
                let row = matrix[i][j];
                rowSum += row;
            try {
                let col = matrix[j][i];
                colSum += col;
            } catch (error) {
                colSum+=matrix[i][j]
            }
        }
        sumRows += rowSum;
        sumCols += colSum;
    }
    console.log(sumRows);
    console.log(sumCols);
    return sumRows === sumCols;
}
//
// console.log(findIfMagical([[4, 5, 6,],
//     [6, 5, 4],
//     [5, 5, 5]]
// ));
// console.log(findIfMagical([[11, 32, 45],
//     [21, 0, 1],
//     [21, 1, 1]]
// ));

console.log(findIfMagical([[1, 0, 0, 3],
    [0, 0, 1,],
    [0, 1, 0,]]
));