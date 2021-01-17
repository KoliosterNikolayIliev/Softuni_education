function evenPosition(array) {
    const result = [];
    for (const arrayElement of array) {
        if(array.indexOf(arrayElement)%2===0){
            result.push(arrayElement)
        }
    }
    return console.log(result.join(' '))
}


evenPosition(['20', '30', '40']);
evenPosition(['5', '10']);