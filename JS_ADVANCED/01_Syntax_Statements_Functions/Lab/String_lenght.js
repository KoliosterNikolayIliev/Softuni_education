function stringLength(...strings){
    let sum = 0;
    let average = 0;
    for (const string of strings) {
        sum+=string.length
    }
    if (sum>0) {
        average = Math.round(sum/strings.length)
    }

    console.log(sum)
    console.log(average)
}

stringLength('chocolate', 'ice cream', 'cake')
stringLength('pasta', '5', '22.3')