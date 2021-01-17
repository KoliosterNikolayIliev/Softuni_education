function array_sort(numbers){
    const newNumbers = []
    for (let number of numbers) {
        if (number<0){
            newNumbers.unshift(number)
        } else {
            newNumbers.push(number)
        }
    }
    return console.log(newNumbers.join('\n'))
}

array_sort([7, -2, 8, 9])
array_sort([3, -2, 0, -1])