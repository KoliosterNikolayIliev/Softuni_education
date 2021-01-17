function findBiggerHalf(array){
    let sortedNumbers = array.sort((a, b) => a-b);
    let biggerArray;
    if (sortedNumbers.length%2 == 0){
        biggerArray = sortedNumbers.slice(sortedNumbers.length/2,sortedNumbers.length)
    } else {
        biggerArray = sortedNumbers.slice(Math.floor(sortedNumbers.length/2),sortedNumbers.length)
    }
    return biggerArray
}

findBiggerHalf([4, 7, 2, 5])
findBiggerHalf([3, 19, 14, 7, 2, 19, 6])