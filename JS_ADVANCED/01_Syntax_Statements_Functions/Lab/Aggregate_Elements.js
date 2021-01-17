function aggregateElements(array){
    let sum = 0;
    let sum1a = 0;
    let concatArr = '';
    for (let argument of array) {
        sum+=argument;
        sum1a+=1/argument;
        concatArr += argument.toString()
    }
    console.log(sum)
    console.log(sum1a)
    console.log(concatArr)
}


aggregateElements([1, 2, 3])
aggregateElements([2, 4, 8, 16])