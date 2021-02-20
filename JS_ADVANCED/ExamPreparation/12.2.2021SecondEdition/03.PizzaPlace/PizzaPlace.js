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


let{assert}=require('chai')

describe("Tests …", function() {
    describe("TODO …", function() {

        it("TODO …", function() {
            obj = {orderedDrink: 'the name of the drink'}
            assert.throw(()=>pizzUni.makeAnOrder(obj), 'You must order at least 1 Pizza to finish the order.')
        });
        it("TODO …", function() {
            obj = {orderedPizza: 'the name of the pizza', orderedDrink: 'the name of the drink'}
            assert.equal(pizzUni.makeAnOrder(obj),'You just ordered the name of the pizza and the name of the drink.')
        });
        it("TODO …", function() {
            obj = {orderedPizza: 'the name of the pizza'}
            assert.equal(pizzUni.makeAnOrder(obj),'You just ordered the name of the pizza')
        });
    });
    describe("TODO …", function() {

        it("TODO …", function() {
            let arr = [{pizzaName: 'margarite', status: 'ready'}]
            assert.equal(pizzUni.getRemainingWork(arr),'All orders are complete!')
        });
        it("TODO …", function() {
            let arr = [{pizzaName: 'margarite', status: 'preparing'}]
            assert.equal(pizzUni.getRemainingWork(arr),'The following pizzas are still preparing: margarite.')
        });
    });
    describe("TODO …", function() {

        it("TODO …", function() {
            assert.equal(pizzUni.orderType(10, 'Carry Out'),9)
        });
        it("TODO …", function() {
            assert.equal(pizzUni.orderType(10, 'Delivery'),10)
        });
    });


});
