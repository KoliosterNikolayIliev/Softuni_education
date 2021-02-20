class Parking {
    constructor(capacity) {
        this.capacity = capacity;
        this.vehicles = [];
    }

    addCar(carModel, carNumber) {
        if (this.capacity === 0) {
            throw new Error("Not enough parking space.");
        }
        let car = {carModel, carNumber, payed: false};
        this.vehicles.push(car);
        this.capacity--;
        return `The ${carModel}, with a registration number ${carNumber}, parked.`;
    }

    removeCar(carNumber) {
        let car = this.vehicles.find(car => car.carNumber === carNumber);
        if (car === undefined) {
            throw new Error("The car, you're looking for, is not found.");
        }
        if (car.payed === false) {
            throw new Error(`${carNumber} needs to pay before leaving the parking lot`);
        }
        this.vehicles.splice(this.vehicles.indexOf(car), 1);
        this.capacity++
        return `${carNumber} left the parking lot.`;
    }

    pay(carNumber) {
        let car = this.vehicles.find(car => car.carNumber === carNumber);
        if (car === undefined) {
            throw new Error(`${carNumber} is not in the parking lot.`);
        }
        if (car.payed===true) {
            throw new Error(`${carNumber}'s driver has already payed his ticket.`);
        }
        car.payed = true;
        return `${carNumber}'s driver successfully payed for his stay.`;
    }

    getStatistics(carNumber) {

        if (carNumber==='') {
            let car = this.vehicles.find(car => car.carNumber === carNumber);
            return `${car.carModel} == ${car.carNumber} - ${car.payed ? 'Has payed' : 'Not payed'}`;
        }
        let result = [`The Parking Lot has ${this.capacity} empty spots left.`];
        let sortedCars = this.vehicles.sort((a, b) => a.carModel.localeCompare(b.carModel));
        for (const car of sortedCars) {
            result.push(`${car.carModel} == ${car.carNumber} - ${car.payed ? 'Has payed' : 'Not payed'}`);
        }
        return result.join('\n');
    }
}

const parking = new Parking(12);

console.log(parking.addCar("Volvo t600", "TX3691CA"));
console.log(parking.addCar("Colvo t600", "TX3691CB"));
console.log(parking.addCar("Aolvo t600", "TX3691CC"));
console.log(parking.addCar("Lolvo t600", "TX3691CG"));
console.log(parking.pay('TX3691CB'));
console.log(parking.removeCar('TX3691CB'));
console.log(parking.getStatistics());

console.log(parking.pay("TX3691CA"));
console.log(parking.removeCar("TX3691CA"));

