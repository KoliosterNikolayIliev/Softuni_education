// function solve(x1, y1, x2, y2) {
//     let to01 = Math.sqrt(x1 ** 2 + y1 ** 2);
//     let to02 = Math.sqrt(x2 ** 2 + y2 ** 2);
//     let x12 = x1 - x2;
//     let y12 = y1 - x2;
//     let xy1Toxy2 = Math.sqrt(x12 ** 2 + y12 ** 2);
//
//     function isValid(number) {
//         return Number.isInteger(number) ? 'is valid' : 'is invalid';
//     }
//
//     let type01 = isValid(to01);
//     let type02 = isValid(to02);
//     let type01to01 = isValid(xy1Toxy2);
//
//     console.log(`{${x1}, ${y1}} to {0, 0} ${type01}`);
//     console.log(`{${x2}, ${y2}} to {0, 0} ${type02}`);
//     console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} ${type01to01}`);
//
// }

function solve(x1, y1, x2, y2) {
    function isValid(x1, y1, x2, y2) {
        let v1 = (x1 - x2) ** 2;
        let v2 = (y1 - y2) ** 2;
        let value = Math.sqrt(v1 + v2);
        return Number.isInteger(value);
    }

    function checkValidity(validity) {
        return validity ? 'valid' : 'invalid';
    }
    console.log(`{${x1}, ${y1}} to {0, 0} is ${checkValidity(isValid(x1, y1, 0, 0))}`);
    console.log(`{${x2}, ${y2}} to {0, 0} is ${checkValidity(isValid(x2, y2, 0, 0))}`);
    console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is ${checkValidity(isValid(x1, y1, x2, y2))}`);
}


// solve(3, 0, 0, 4);
// solve(2, 1, 1, 1);
solve(3.3, 0, 0, 4);

