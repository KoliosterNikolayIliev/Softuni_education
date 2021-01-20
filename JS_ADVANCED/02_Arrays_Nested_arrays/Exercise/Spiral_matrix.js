function spiral(rows, cols) {
    let total = rows * cols;
    let matrix = [];

    for (let i = 0; i < rows; i++) {
        matrix.push([]);
        for (let j = 0; j < cols; j++) {
            matrix[i][j] = 0;
        }
    }

    let x = 0;
    let y = 0;
    let step = 0;
    for (let i = 0; i < total;) {
        while (y + step < cols) {
            i++;
            matrix[x][y] = i;
            y++;
        }
        y--;
        x++;
        while (x + step < rows) {
            i++;
            matrix[x][y] = i;
            x++;
        }
        x--;
        y--;
        while (y >= step) {
            i++;
            matrix[x][y] = i;
            y--;
        }
        y++;
        x--;
        step++;
        while (x >= step) {
            i++;
            matrix[x][y] = i;
            x--;
        }
        x++;
        y++;
    }
    return matrix.map(row => row.join(" ")).join("\n");
}

console.log(spiral(5, 5) + '\n');
console.log(spiral(3, 3) + '\n');

