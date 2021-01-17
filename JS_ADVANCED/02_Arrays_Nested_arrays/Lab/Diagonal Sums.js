function findDiagonalSum(matrix) {
    let sumMain = 0;
    let sumSecondary = 0;
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j <= matrix[i].length - 1; j++) {
            if (j === i) {
                sumMain += matrix[i][j];
            }
        }
    }
    for (let i = 0; i < matrix.length; i++) {
        for (let j = matrix.length - 1; j >= 0; j--) {
            if (i + j === matrix.length - 1) {
                sumSecondary += matrix[i][j];
            }

        }
    }
    console.log(sumMain + ' ' + sumSecondary);
}

// findDiagonalSum([[20, 40],
//     [10, 60]]
// );
// findDiagonalSum([[3, 5, 17],
//     [-1, 7, 14],
//     [1, -8, 89]]
// )

findDiagonalSum([[20, 40, 60, 80], [20, 40, 60, 80], [20, 40, 60, 80], [20, 40, 60, 80]]);