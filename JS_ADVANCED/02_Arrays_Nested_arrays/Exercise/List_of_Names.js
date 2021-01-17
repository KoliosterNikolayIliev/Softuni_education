function sortListAcc(array){
    array.sort((a, b) => a.localeCompare(b));
    let counter = 1
    for (let arrayElement of array) {
        console.log(counter+'.'+arrayElement)
        counter++
    }
}

sortListAcc(["John", "Bob", "Christina", "Ema"]);