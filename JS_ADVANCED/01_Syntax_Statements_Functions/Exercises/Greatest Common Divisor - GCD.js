function gcd(numberOne, numberTwo){
    let divider = 1
    for (let i = 2; i <= numberOne ; i++) {
        if (numberOne % i === 0 && numberTwo % i === 0){
            divider = i
        }
    }
    return divider;
}

// function gcd(numberOne, numberTwo) {
//     return !numberTwo ? numberOne : gcd(numberTwo, numberOne % numberTwo)
// }

console.log(gcd(15, 5));
console.log(gcd(2154, 458));