function calorieObject(array) {
    const food = array.filter(el => array.indexOf(el) % 2 === 0);
    const calories = array.filter(el => array.indexOf(el) % 2 !== 0);
    const calorieContent = {};
    for (let i = 0; i < food.length; i++) {
        calorieContent[food[i]] = Number(calories[i]);
    }
    return calorieContent;
}

console.log(calorieObject(['Yoghurt', '48', 'Rise', '138', 'Apple', '52']));
console.log(calorieObject(['Potato', '93', 'Skyr', '63', 'Cucumber', '18', 'Milk', '42']));