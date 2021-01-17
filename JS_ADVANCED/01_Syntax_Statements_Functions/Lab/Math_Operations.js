function calculator(numOne, numTwo, operator){
    let result;
    switch (operator){

        case '+': result = numOne + numTwo;
            break;
        case '-': result = numOne - numTwo;
            break;
        case '/': result = numOne / numTwo;
            break;
        case '*': result = numOne * numTwo;
            break;
        case '**': result = numOne ** numTwo;
            break;
        case '%': result = numOne % numTwo;
            break;
    }
    console.log(result)
}

calculator(5, 6, '+')
calculator(3, 5.5, '*')