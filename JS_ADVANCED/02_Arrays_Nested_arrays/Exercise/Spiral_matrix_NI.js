function spiral(rows, cols) {
    let matrix = [];

    for (let i = 0; i < rows; i++) {
        matrix.push([]);
        for (let j = 0; j < cols; j++) {
            matrix[i][j] = 0;
        }
    }
    let counter = 1;
    let startColumn = 0;
    let endColumn = cols - 1;
    let startRow = 0;
    let endRow = rows - 1;
    while (startColumn <= endColumn && startRow <= endRow) {

        for (let i = startColumn; i <= endColumn; i++) {
            matrix[startRow][i] = counter;
            counter++;
        }
        startRow++;

        for (let i = startRow; i <= endRow; i++) {
            matrix[i][endColumn] = counter;
            counter++;
        }
        endColumn--;

        for (let i = endColumn; i >= startColumn; i--) {
            matrix[endRow][i] = counter;
            counter++;
        }
        endRow--;

        for (let i = endRow; i >= startRow; i--) {
            matrix[i][startColumn] = counter;
            counter++;
        }
        startColumn++;
    }

    return matrix.map(row => row.join(" ")).join("\n");
}

console.log(spiral(5, 5) + '\n');
console.log(spiral(3, 3) + '\n');