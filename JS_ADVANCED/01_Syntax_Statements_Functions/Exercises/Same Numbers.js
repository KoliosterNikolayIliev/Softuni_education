function checkNumbers(number){
    let numberArray = number.toString().split('');
    numberArray=numberArray.map(x=> parseInt(x));
    let boolValue = true;
    let sum = 0
    for (const numberElement of numberArray) {
        if (numberArray[0] !== numberElement){
            boolValue = false;
            break;
        }
    }
    for (const numberElement of numberArray) {
        sum+=numberElement;
    }
    console.log(boolValue)
    console.log(sum)
}
checkNumbers(2222222)
checkNumbers(1234)