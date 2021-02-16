let name = 'Marketing'

departments = [
    {Marketing:[{name: 'Pesho', salary:100, position:'engineer'},{}]},
    {Engineering:[{name: 'Gosho', salary:100, position:'engineer'},{}]}
    ]

let key = Object.keys(departments[0]).valueOf()
console.log(typeof key);