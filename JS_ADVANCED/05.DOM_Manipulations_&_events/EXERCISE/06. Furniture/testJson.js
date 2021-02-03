// const sharePersonalInfo = function (...activities) {
//     let info = `Hello, my name is ${firstPerson.name} and` + ` I'm a ${firstPerson.profession}.\n`;
//     info += activities.reduce((acc, curr) => {let el = `--- ${curr}\n`;return acc + el;}, "My hobbies are:\n").trim();return info;};
//
// const firstPerson = {name: "Peter", profession: "Fisherman"};
// console.log(sharePersonalInfo.call(firstPerson, 'biking', 'swimming', 'football'));

// const x = 42;
// const getX = function () {
//     return this.x;
// };
// const module = {x, getX};
// const unboundGetX = module.getX;
// console.log(unboundGetX());
// const boundGetX = unboundGetX.bind(module);
// console.log(boundGetX());

// function myFunc(){
//     console.log(this);
// }
// function  outer(){
//     myFunc();
// }
//
// const myObj = {
//     name:'kur',
//     myFunc
// };
//
// myObj.myFunc()

// const myObj = {
//     name: 'Pesho',
//     outerFunc(){
//         console.log(this+'100');
//
//         myFunc();
//
//         function  myFunc(){
//             console.log(this+'200')
//         }
//     }
// }
// myObj.outerFunc()

// const myObj = {
//     name: 'Pesho',
//     outerFunc(...args) {
//         console.log(this + '100');
//         // const inner = () => {console.log(this + '200');}
//         const inner = function(...args){
//             if (args.length>0){
//             console.log(args)
//             }else{
//                 console.log(this + '200')
//             }
//         }
//         inner(...args)
//     }
// };
// myObj.outerFunc();
// func =  () =>{console.log(this)}
// func.call(myObj)
// func.apply(myObj)

// const myObj = {
//     name: 'Pesho'
// };
//
// function myFunc(a,b) {
//     console.log(this)
//     console.log(a,b);
// }
// myFunc(1,3)
// myFunc.apply(myObj,[3,4])
// myFunc.call(myObj,...[3,4])
// const bound = myFunc.bind(myObj,55,33)
// bound(66,3)
//
// let pleaseLetMe = 'kur'
// console.log(pleaseLetMe);

// function sayHello (){
//     return 'Hello, ';
// }
//
// function  greeting (message, name){
//     return message()+ name;
// }
//
// console.log(greeting(sayHello,'JS'))

// function getgreet() {
//     return syhi()
//     function syhi() {
//         console.log('hi');
//     }
// }
// getgreet()
// const returngr = getgreet()


// function A() {
//     B();
//     let myVarA = 5;
//     console.log('inside A', myVarA);
//
// }
//
// function B() {
//     C();
//     let myVarB = 3;
//     console.log('inside B', myVarB);
//
// }
//
// function C() {
//     let myVarC = 'Joro';
//     console.log('inside C', myVarC);
// }
//
// A();

// function A() {
//     let myVarA = 5;
//     console.log('inside A', myVarA);
//     return B();
//
//     function B() {
//         let myVarB = 3;
//         console.log('inside B', myVarB, myVarA);
//     }
//
// }
//
// const outsideB = A;
// outsideB()


function createRect(width, height){
    return {getHeight, getWidth, setWidth}

    function setWidth(value){
        width = value
    }

    function getWidth(){
        return width;
    }

    function getHeight(){
        return height;
    }
}

const myRect = createRect(5,3)
console.log(myRect);
console.log(myRect.getHeight());
myRect.setWidth(7)
console.log(myRect.getWidth());
