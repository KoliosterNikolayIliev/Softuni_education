function orbit(array) {
    let rows = array[0];
    let cols = array[1];
    let x = array[2];
    let y = array[3];

    const movements = {
        'up': [-1, 0], 'down': [1, 0], 'left': [0, -1],
        'right': [0, 1], 'upLeft': [-1, -1], 'upRight': [-1, 1], 'downLeft': [1, -1], 'downRight': [1, 1]
    };
    let matrix = [];
    for (let i = 0; i < rows; i++) {
        matrix.push([]);
        for (let j = 0; j < cols; j++) {
            matrix[i].push(0);
        }
    }

    matrix[y][x] = 1;
    let number = 2;
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            for (const move in movements) {
                x = array[2];
                y = array[3];
                y += movements[move][0];
                x += movements[move][1];
                try {
                    if (matrix[y][x] === 0 && move !== undefined) {
                        matrix[y][x] = number;
                    }

                } catch (error) {
                }
            }
            for (const move in movements) {
                if (move === 'up') {
                    movements[move][0] -= 1;
                } else if (move === 'down') {
                    movements[move][0] += 1;
                } else if (move === 'left') {
                    movements[move][1] -= 1;
                } else if (move === 'right') {
                    movements[move][1] += 1;
                } else if (move === 'upLeft') {
                    movements[move][0] -= 1;
                    movements[move][1] -= 1;
                } else if (move === 'upRight') {
                    movements[move][0] -= 1;
                    movements[move][1] += 1;
                } else if (move === 'downLeft') {
                    movements[move][0] += 1;
                    movements[move][1] -= 1;
                } else if (move === 'downRight') {
                    movements[move][0] += 1;
                    movements[move][1] += 1;
                }

            }
            number+=1

        }
    }


    // matrix[y][x] = 1
    // matrix[0][1] = 2
    // matrix[1][0] = 2
    // matrix[1][1] = 2
    // matrix[0][2] = 3
    // matrix[1][2] = 3
    // matrix[2][2] = 3
    // matrix[2][1] = 3
    // matrix[2][0] = 3

    return returnPrintable(matrix).join('\n');
    function returnPrintable(matrix) {
        const elements = [];
        for (let element of matrix) {
            elements.push(element.join(' '));
        }
        return elements;}


}



console.log(orbit([4, 4, 0, 0]) + '\n');
console.log(orbit([5, 5, 2, 2]) + '\n');
console.log(orbit([3, 3, 2, 2]) + '\n');