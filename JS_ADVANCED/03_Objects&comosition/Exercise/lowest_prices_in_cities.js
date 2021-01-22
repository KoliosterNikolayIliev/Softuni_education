function priceCheck(input) {
    let products = {};
    let lowestPricesTowns = {};
    let townsArr = input.map(el => el.split(' | '));
    for (const data of townsArr) {
        if (!products[data[1]]) {
            products[data[1]] = [{town: data[0], price: data[2]}];
        } else {
            products[data[1]].push({town: data[0], price: data[2]});
        }
    }
    for (const product in products) {
        for (const obj of products[product]) {
            if(lowestPricesTowns[product]){
                if (Number(lowestPricesTowns[product][1])>Number(obj.price)){
                    lowestPricesTowns[product] = [obj.town,Number(obj.price)]
                }
            }else{
                lowestPricesTowns[product] = [obj.town,Number(obj.price)]
            }


        }

    }
    let result = ''
    for (const product in lowestPricesTowns) {
        result+=`${product} -> ${lowestPricesTowns[product][1]} (${lowestPricesTowns[product][0]})\n`
    }
    return result
}




console.log(priceCheck(['Sample Town | Sample Product | 1000',
    'Sample Town | Orange | 2',
    'Sample Town | Peach | 1',
    'Sofia | Orange | 3',
    'Sofia | Peach | 2',
    'New York | Sample Product | 1000.1',
    'New York | Burger | 10',
    'Sofia | Burger | 10']
));