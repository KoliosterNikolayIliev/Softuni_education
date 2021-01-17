function diagonalAttack(array) {
    let matrix = [];
    for (const el of array) {
        let matElem = el.split(' ');
        let numEl = matElem.map(el => Number(el));
        matrix.push(numEl);
    }

    let matrixData = findDiagonalSum(matrix);
    if (matrixData['sums'][0] !== matrixData['sums'][1]) {
        return returnPrintable(matrix).join('\n');
    } else {
        for (let i = 0; i < matrix.length; i++) {
            for (let j = 0; j <= matrix[i].length - 1; j++) {
                if (!matrixData['diagonals'].includes([i, j].join(' '))) {
                    matrix[i][j] = matrixData['sums'][0];
                }
            }
        }
        return returnPrintable(matrix).join('\n');
    }

    function findDiagonalSum(matrix) {
        let diagonals = [];
        let sumMain = 0;
        let sumSecondary = 0;
        for (let i = 0; i < matrix.length; i++) {
            for (let j = 0; j <= matrix[i].length - 1; j++) {
                if (j === i) {
                    sumMain += matrix[i][j];
                    diagonals.push([i, j].join(' '));
                }
            }
        }
        for (let i = 0; i < matrix.length; i++) {
            for (let j = matrix.length - 1; j >= 0; j--) {
                if (i + j === matrix.length - 1) {
                    sumSecondary += matrix[i][j];
                    diagonals.push([i, j].join(' '));
                }

            }
        }
        return {sums: [sumMain, sumSecondary], diagonals: diagonals};
    }

    function returnPrintable(matrix) {
        const elements = [];
        for (let element of matrix) {
            elements.push(element.join(' '));
        }
        return elements;
    }
}

console.log(diagonalAttack(['5 3 12 3 1', '11 4 23 2 5', '101 12 3 21 10', '1 4 5 2 2', '5 22 33 11 1']));

console.log(diagonalAttack(['1 1 1', '1 1 1', '1 1 0']));


