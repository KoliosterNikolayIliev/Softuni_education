function orbit(array) {
    let rows = array[0];
    let cols = array[1];
    let starRow = array[2];
    let starCol = array[3];

    let matrix = [];
    for(let i=0; i<rows; i++) {
        matrix.push([]);
    }

    for(let row = 0; row< rows; row++) {
        for(let col=0; col<cols; col++) {
            matrix[row][col] = Math.max(Math.abs(row - starRow), Math.abs(col - starCol)) + 1;
        }
    }

    return matrix.map(row => row.join(" ")).join("\n");
}



console.log(orbit([4, 4, 0, 0]) + '\n');
console.log(orbit([5, 5, 2, 2]) + '\n');
console.log(orbit([3, 3, 2, 2]) + '\n');