function ticTacToe(moves) {
    let playTable = [[false, false, false],
        [false, false, false],
        [false, false, false]];
    let counter = 0;
    let player;
    let win = false;

    while (moves.length) {
        if (counter % 2 === 0) {
            player = 'X';
        } else {
            player = 'O';
        }
        let pos = moves.shift();
        let x = Number(pos[2]);
        let y = Number(pos[0]);
        if (playTable[y][x] === false) {
            playTable[y][x] = player;
            counter++;
        } else {
            let flattened = playTable.flat()
            let timeToBreak = flattened.includes(false);
            if (timeToBreak === false){
                break
            }else{
                console.log("This place is already taken. Please choose another!");
            }

        }
        if (playTable[0][0] === playTable[0][1] && playTable[0][0] === playTable[0][2] && playTable[0][0] === player) {
            win = true;
        } else if (playTable[1][0] === playTable[1][1] && playTable[1][0] === playTable[1][2] && playTable[1][0] === player) {
            win = true;
        } else if (playTable[2][0] === playTable[2][1] && playTable[2][0] === playTable[2][2] && playTable[2][0] === player) {
            win = true;
        } else if (playTable[0][0] === playTable[1][1] && playTable[0][0] === playTable[2][2] && playTable[0][0] === player) {
            win = true;
        } else if (playTable[2][0] === playTable[1][1] && playTable[2][0] === playTable[0][2] && playTable[2][0] === player) {
            win = true;
        } else if (playTable[0][0] === playTable[1][0] && playTable[0][0] === playTable[2][0] && playTable[0][0] === player) {
            win = true;
        } else if (playTable[0][2] === playTable[1][2] && playTable[0][2] === playTable[2][2] && playTable[0][2] === player) {
            win = true;
        }

        if (win) {
            break;
        }

    }
    if (win) {
        return `Player ${player} wins! \n${printMatrix(playTable)}`;
    }
    return `The game ended! Nobody wins :( \n${printMatrix(playTable)}`;

    function printMatrix(matrix) {
        let result=''
        for (const el of matrix) {
            result+= el.join('\t') + '\n';
        }
        return result;
    }
}



console.log(ticTacToe(["0 1",
    "0 0",
    "0 2",
    "2 0",
    "1 0",
    "1 1",
    "1 2",
    "2 2",
    "2 1",
    "0 0"]
));
console.log(ticTacToe(["0 0",
    "0 0",
    "1 1",
    "0 1",
    "1 2",
    "0 2",
    "2 2",
    "1 2",
    "2 2",
    "2 1"]
));
console.log(ticTacToe(["0 1",
    "0 0",
    "0 2",
    "2 0",
    "1 0",
    "1 2",
    "1 1",
    "2 1",
    "2 2",
    "0 0"]
));

