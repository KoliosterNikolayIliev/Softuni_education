function speed_test(speed, area) {
    speed = Number(speed)
    let restrictions = {'motorway': 130, 'residential': 20, 'interstate': 90, 'city': 50};
    let speedDifference = speed - restrictions[area];
    let status;
    if (speedDifference >= 1 && speedDifference <= 20) {
        status = 'speeding';
    } else if (speedDifference > 20 && speedDifference <= 40) {
        status = 'excessive speeding';
    } else if (speedDifference <= 0) {
        return console.log(`Driving ${speed} km/h in a ${restrictions[area]} zone`);
    } else {
        status = 'reckless driving';
    }
    return console.log(`The speed is ${speedDifference} km/h faster than the allowed speed of ${restrictions[area]} - ${status}`);
}

speed_test(70, 'city')
speed_test(21, 'residential')
speed_test(140, 'interstate')
speed_test(171, 'motorway')