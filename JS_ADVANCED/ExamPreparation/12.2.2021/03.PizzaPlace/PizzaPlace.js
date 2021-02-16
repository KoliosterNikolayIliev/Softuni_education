let pizzUni = {
    makeAnOrder: function (obj) {
        if (!obj.orderedPizza) {
            throw new Error('You must order at least 1 Pizza to finish the order.');
        } else {
            let result = `You just ordered ${obj.orderedPizza}`
            if (obj.orderedDrink) {
                result += ` and ${obj.orderedDrink}.`
            }
            return result;
        }
    },
    getRemainingWork: function (statusArr) {

        const remainingArr = statusArr.filter(s => s.status != 'ready');

        if (remainingArr.length > 0) {
            let pizzaNames = remainingArr.map(p => p.pizzaName).join(', ')
            let pizzasLeft = `The following pizzas are still preparing: ${pizzaNames}.`

            return pizzasLeft;
        } else {
            return 'All orders are complete!'
        }
    },
    orderType: function (totalSum, typeOfOrder) {
        if (typeOfOrder === 'Carry Out') {
            totalSum -= totalSum * 0.1;

            return totalSum;
        } else if (typeOfOrder === 'Delivery') {

            return totalSum;
        }
    }
}

//1.)
// let obj = {orderedPizza: 'margarita', orderedDrink: 'coffee'}
// console.log(pizzUni.makeAnOrder(obj));
//
// let obj2 = {orderedPizza: 'margarita'}
// console.log(pizzUni.makeAnOrder(obj2));
//
// obj3 = {orderedDrink: 'coffee'}
// pizzUni.makeAnOrder(obj3)
//
// obj4 = {}
// pizzUni.makeAnOrder(obj4)

//2.)
// let arr = [{pizzaName:'margarita', status:'ready'},{pizzaName:'margarita', status:'not ready'}]
// let arr2 = [{pizzaName:'margarita', status:'ready'},{pizzaName:'margarita', status:'ready'}]
//
// console.log(pizzUni.getRemainingWork(arr));
// console.log(pizzUni.getRemainingWork(arr2));
//3.)

// console.log(pizzUni.orderType(50, 'Carry Out'));
// console.log(pizzUni.orderType(50, 'Delivery'));



let{assert}=require('chai')

describe("Tests …", function() {
    describe("makeAnOrder", function() {

        it("asserts happy", function() {
            let obj = {orderedPizza: 'margarita', orderedDrink: 'coffee'}
            assert.equal(pizzUni.makeAnOrder(obj), `You just ordered margarita and coffee.`)
        });
        it("asserts pizza only", function() {
            let obj = {orderedPizza: 'margarita'}
            assert.equal(pizzUni.makeAnOrder(obj), `You just ordered margarita`)
        });
        it("asserts without pizza", function() {
            let obj = {orderedDrink: 'coffee'}
            assert.throws(()=>pizzUni.makeAnOrder(obj), 'You must order at least 1 Pizza to finish the order.')
        });
        it("asserts empty obj", function() {
            let obj = {}
            assert.throws(()=>pizzUni.makeAnOrder(obj), 'You must order at least 1 Pizza to finish the order.')
        });
    });

    describe("getRemainingWork", function() {

        it("asserts not done", function() {
            let arr = [{pizzaName:'margarita', status:'ready'},{pizzaName:'margarita', status:'not ready'}]
            assert.equal(pizzUni.getRemainingWork(arr), 'The following pizzas are still preparing: margarita.')
        });
        it("asserts not done", function() {
            let arr = [{pizzaName:'margarita', status:'ready'},{pizzaName:'margarita', status:'ready'}]
            assert.equal(pizzUni.getRemainingWork(arr), 'All orders are complete!')
        });

    });
    describe("orderType", function() {

        it("discount", function() {
            assert.equal(pizzUni.orderType(50, 'Carry Out'), 45)
        });
        it("discount", function() {
            assert.equal(pizzUni.orderType(50, 'Delivery'), 50)
        });

    });
});

