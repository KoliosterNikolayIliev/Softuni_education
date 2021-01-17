function priceCalc(fruit, weightGrams, pricePerKilo){
    let weightKilograms = weightGrams/1000
    let moneyNeeded = pricePerKilo*weightKilograms
    console.log(`I need $${moneyNeeded.toFixed(2)} to buy ${weightKilograms.toFixed(2)} kilograms ${fruit}.`)

}

priceCalc('orange', 2500, 1.80)
priceCalc('apple', 1563, 2.35)
