class Parking {
    constructor(capacity) {
        this.capacity = capacity;
        this.vehicles = [];
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
        let index = this.vehicles.findIndex(car => car.carNumber === carNumber);
        if (index === -1) {
            throw new Error("The car, you're looking for, is not found.");
        }
        let car = this.vehicles[index];
        if (!car.payed) {
            throw new Error(`${carNumber} needs to pay before leaving the parking lot.`);
        }
        this.capacity += 1;
        this.vehicles.splice(index, 1);
        return `${carNumber} left the parking lot.`;
    }

    pay(carNumber) {
        let index = this.vehicles.findIndex(car => car.carNumber === carNumber);
        if (index === -1) {
            throw new Error(`${carNumber} is not in the parking lot.`);
        }
        let car = this.vehicles[index];
        if (car.payed) {
            throw new Error(`${carNumber}'s driver has already payed his ticket.`);
        }
        car.payed = true;
        return `${carNumber}'s driver successfully payed for his stay.`;
    }

    getStatistics(carNumber) {
        let result;
        if (!carNumber) {
            result = `The Parking Lot has ${this.capacity} empty spots left.`;
            let cars = this.vehicles.sort((a, b) => a.carModel - b.carModel);
            for (const car of cars) {
                result += `\n${car.carModel} == ${car.carNumber} - ${car.payed ? 'Has payed' : 'Not payed'}`;
            }
        } else {
            let car = this.vehicles.find(car => car.carNumber === carNumber);
            result = `${car.carModel} == ${carNumber} - ${car.payed ? 'Has payed' : 'Not payed'}`;
        }
        return result;
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



