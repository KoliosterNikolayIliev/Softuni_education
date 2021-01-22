function produce(obj) {
    const car = {};
    const engines = {
        smallEngine: {power: 90, volume: 1800},
        normalEngine: {power: 120, volume: 2400},
        monsterEngine: {power: 200, volume: 3500}
    };
    const carriages = {
        hatchback: {type: 'hatchback', color: 'as required'},
        coupe: {type: 'coupe', color: 'as required'}
    };
    car.model = obj.model;
    car.engine = chooseEngine(obj.power);
    car.carriage = chooseCarriage(obj.carriage, obj.color);
    car.wheels = chooseWheels(obj.wheelsize);

    function chooseEngine(power) {
        for (let engine in engines) {
            if (power === engines[engine].power || power < engines[engine].power){
                return engines[engine]
            }
        }
    }


function chooseCarriage(carriageType, color) {
    for (const carriage in carriages) {
        if (carriageType === carriages[carriage].type){
            let newCarriage = carriages[carriage]
            newCarriage.color = color
            return newCarriage
        }

    }

}

function chooseWheels(wheelSize) {
        if (wheelSize%2 ===0){
            wheelSize--
        }
        return Array(4).fill(wheelSize)
}


return car;
}

console.log(produce({
        model: 'VW Golf II',
        power: 90,
        color: 'blue',
        carriage: 'hatchback',
        wheelsize: 14
    }
));
console.log(produce({
        model: 'Opel Vectra',
        power: 110,
        color: 'grey',
        carriage: 'coupe',
        wheelsize: 17
    }
));