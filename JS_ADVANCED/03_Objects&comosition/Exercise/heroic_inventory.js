function heroData(rawData) {

    let heroes = [];
    rawData = rawData.map(el => el.split(' / '));
    for (const hero of rawData) {
        let heroData = {};
        heroData.name = hero[0];
        heroData.level = Number(hero[1]);
        heroData.items = hero[2]?hero[2].split(', '):[];
        heroes.push(heroData);
    }
    let output = JSON.stringify(heroes);
    return output;
}

console.log(heroData(['Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara']
));
console.log(heroData(['Jake / 1000 / Gauss, HolidayGrenade']));