function townPopulation(array) {
    const cities = {};
    let cityArr;
    for (const city of array) {
        cityArr = city.split(' <-> ');
        if (cities[cityArr[0]] !== undefined) {
            cities[cityArr[0]] += Number(cityArr[1]);
        } else {
            cities[cityArr[0]] = Number(cityArr[1]);
        }

    }
    for (let city in cities) {
        console.log(`${city} : ${cities[city]}`);

    }
}

townPopulation(['Sofia <-> 1200000',
    'Montana <-> 20000',
    'New York <-> 10000000',
    'Washington <-> 2345000',
    'Las Vegas <-> 1000000']
);
townPopulation(['Istanbul <-> 100000',
    'Honk Kong <-> 2100004',
    'Jerusalem <-> 2352344',
    'Mexico City <-> 23401925',
    'Istanbul <-> 1000']
);
