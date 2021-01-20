// function createRecord(name, population, treasury) {
//     return {
//         name, population, treasury,
//         taxRate: 10,
//         collectTaxes() {
//             this.treasury += this.population * this.taxRate;
//         },
//         applyGrowth(percent) {
//             this.population += Math.floor(this.population * percent / 100);
//         },
//         applyRecession(percent) {
//             this.treasury -= Math.floor(this.treasury * percent / 100);
//         },
//     };
// }

function createRecord(name, population, treasury) {
    const city = {
        name, population, treasury,
        taxRate: 10,
        
    };
    city.collectTaxes = function () {
        return city.treasury += city.population * city.taxRate;
    };
    city.applyGrowth = function (percent) {
        return city.population += Math.floor(city.population * percent / 100);
    };
    city.applyRecession = function (percent) {
        city.treasury -= Math.floor(city.treasury * percent / 100);
    };
    return city
}


console.log(createRecord('Tortuga',
    7000,
    15000
));


const city =
    createRecord('Tortuga',
        7000,
        15000);
city.collectTaxes();
console.log(city.treasury);
city.applyGrowth(5);
console.log(city.population);

