class Parking {
    constructor(capacity) {
        this.capacity = capacity;
        this.vechicles = [];
    }

    addCar(carModel, carNumber) {
        if (this.capacity === 0) {
            throw new Error('Not enough parking space.');
        }
        this.vehicles.push({carModel, carNumber, payed: false});
        this.capacity--;

        return `The ${carModel}, with a registration number ${carNumber}, parked.`;
    }

    removeCar(carNumber) {

    }

    pay(carNumber) {

    }

    getStatistics(carNumber) {

    }
}

// const parking = new Parking(3);
//
// console.log(parking.addCar("Aolvo t600", "TX3691CA"));
// console.log(parking.addCar("Volvo t600", "TX3691CB"));
// console.log(parking.addCar("Volvo t600", "TX3691CC"));
// console.log(parking.pay("TX3691CB"));
// console.log(parking.pay("TX3691Ck"));

const parking = new Parking(12);

console.log(parking.addCar("Volvo t600", "TX3691CA"));
console.log(parking.addCar("Aolvo t600", "TX3691CA"));
console.log(parking.addCar("Bolvo t600", "TX3691CA"));
console.log(parking.getStatistics());

console.log(parking.pay("TX3691CA"));
console.log(parking.removeCar("TX3691CA"));



