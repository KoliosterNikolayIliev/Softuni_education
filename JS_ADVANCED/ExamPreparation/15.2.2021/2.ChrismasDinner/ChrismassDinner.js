class ChristmasDinner{
    constructor(budget) {
        this.budget = budget
        this.dishes =[]
        this.products=[]
        this.guests = {}
    }
    set budget(value){
        if (value<0){
            throw new Error("The budget cannot be a negative number")
        }
        this._budget = value
    }
    get budget(){
        return this._budget
    }
    shopping(productPrice){
        if (productPrice[1]>this.budget){
            throw new Error("Not enough money to buy this product")
        }
        this.products.push(productPrice[0])
        this.budget-=productPrice[1]
        return `You have successfully bought ${productPrice[0]}!`
    }
    recipes(recipe){
        let productsList = recipe.productsList
        let recipeName = recipe.recipeName
        for (let pr of productsList){
            if (!this.products.includes(pr)){
                throw new Error("We do not have this product")
            }
        }
        this.dishes.push({recipeName,productsList})
        return `${recipeName} has been successfully cooked!`
    }
    inviteGuests(name, dish){
        let currentDish = this.dishes.find(d=>d.recipeName===dish)
        if (currentDish===undefined){
            throw new Error("We do not have this dish")
        }
        if (this.guests[name]){
            throw new Error("This guest has already been invited")
        }
        this.guests[name]=currentDish.recipeName
        return `You have successfully invited ${name}!`
    }
    showAttendance(){
        let result =[]
        for (const [key,value] of Object.entries(this.guests)) {
            let products;
            for (const dish of this.dishes) {
                if (dish.recipeName == value){
                    products = dish.productsList.join(', ')
                }
            }
            result.push(`${key} will eat ${value}, which consists of ${products}`)
        }
        return result.join('\n')
    }
}

let dinner = new ChristmasDinner(300);

dinner.shopping(['Salt', 1]);
dinner.shopping(['Beans', 3]);
dinner.shopping(['Cabbage', 4]);
dinner.shopping(['Rice', 2]);
dinner.shopping(['Savory', 1]);
dinner.shopping(['Peppers', 1]);
dinner.shopping(['Fruits', 40]);
dinner.shopping(['Honey', 10]);

dinner.recipes({
    recipeName: 'Oshav',
    productsList: ['Fruits', 'Honey']
});
dinner.recipes({
    recipeName: 'Folded cabbage leaves filled with rice',
    productsList: ['Cabbage', 'Rice', 'Salt', 'Savory']
});

dinner.recipes({
    recipeName: 'Peppers filled with beans',
    productsList: ['Beans', 'Peppers', 'Salt']
});
//
dinner.inviteGuests('Ivan', 'Oshav');
dinner.inviteGuests('Petar', 'Folded cabbage leaves filled with rice');
dinner.inviteGuests('Georgi', 'Peppers filled with beans');
console.log(dinner.showAttendance());

// let a = [{pesho:12},{kiro:14}]
// c = []
// for (const el of a) {
//     console.log(Object.entries(el)[0])
// }


