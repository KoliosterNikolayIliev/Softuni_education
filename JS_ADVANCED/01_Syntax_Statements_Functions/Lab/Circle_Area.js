function findCircleArea(radius){
    if (typeof radius === 'number'){
        let result = Math.PI*radius**2
        let roundedResult = result.toFixed(2)
        console.log(roundedResult)
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${typeof radius}.`)
    }
}

findCircleArea(5)
findCircleArea('name')


