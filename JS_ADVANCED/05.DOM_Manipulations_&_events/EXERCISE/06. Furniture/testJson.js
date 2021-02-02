// const sharePersonalInfo = function (...activities) {
//     let info = `Hello, my name is ${firstPerson.name} and` + ` I'm a ${firstPerson.profession}.\n`;
//     info += activities.reduce((acc, curr) => {let el = `--- ${curr}\n`;return acc + el;}, "My hobbies are:\n").trim();return info;};
//
// const firstPerson = {name: "Peter", profession: "Fisherman"};
// console.log(sharePersonalInfo.call(firstPerson, 'biking', 'swimming', 'football'));

const x = 42;
const getX = function () {
    return this.x;
};
const module = {x, getX};
const unboundGetX = module.getX;
console.log(unboundGetX());
const boundGetX = unboundGetX.bind(module);
console.log(boundGetX());

