// let a = ['2021/11/03', '1983/12/24','1983/01/01']
// let b = a.sort()
// let c = a.sort(compareNumbers)
// let d = a.sort(compareNonAsci)
//
// function compareNumbers(a, b) {
//     return a - b;
// }
//
// function compareNonAsci(a, b) {
//     return a.localeCompare(b);
// }
//
// console.log(a);
// console.log(b);
// console.log(c);
// console.log(d);

//Filter
// const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];
//
// const result = words.filter((word) => word.length > 6);


// let vechicles = [['sedan', 'ca22', {payed:false}],['sedan1', 'ca221', {payed:false}],['seda2n', 'ca223', {payed:false}]]
// // console.log(vechicles);
// for (const car of vechicles) {
//     if (car[1]==='ca221' && car[2].payed===false){
//         let a = vechicles.splice(vechicles.indexOf(car),1)
//         // console.log(a[0]);
//     }
// }
// let car = vechicles.filter(car=>car[1] ==='ca22')
// console.log(car[0]);
// // console.log(vechicles);
//
// MAP FILTER TOGETHER
// find
// findindex

class Parking {
    constructor(capacity) {
        this.capacity = capacity;
        this.vechicles = [];
    }
    addCar(carModel, carNumber) {
        if (!carModel){
            this.capacity = 0
        }
    }
}

let a = new Parking(10)
console.log(a.capacity);
a.addCar(false, 12)
console.log(a.capacity);