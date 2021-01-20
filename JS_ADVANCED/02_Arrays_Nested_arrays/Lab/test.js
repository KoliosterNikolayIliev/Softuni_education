// let a = true
// console.log(typeof (a));
// console.log(a);
//
// a = false
//
// console.log(typeof (a));
// console.log(a);
//
// let b = true
//
// if(a===b){
//     console.log(kur);
// }
//
// // Deep copy recursive function !!!
// function deepCopy(target) {
//     if (Array.isArray(target)) {
//         return target.map(deepCopy);
//     } else if (typeof target == 'object') {
//         return [...Object.entries(target)].reduce((a, [k,v]) => Object.assign(a, {[k]: deepCopy(v)}), {});
//     } else {
//         return target;
//     }
// }


//Deep copy from MDN !!!

// function test() {
//     'use strict';
//
//     let obj1 = { a: 0 , b: { c: 0}};
//     let obj2 = Object.assign({}, obj1);
//     console.log(JSON.stringify(obj2)); // { "a": 0, "b": { "c": 0}}
//
//     obj1.a = 1;
//     console.log(JSON.stringify(obj1)); // { "a": 1, "b": { "c": 0}}
//     console.log(JSON.stringify(obj2)); // { "a": 0, "b": { "c": 0}}
//
//     obj2.a = 2;
//     console.log(JSON.stringify(obj1)); // { "a": 1, "b": { "c": 0}}
//     console.log(JSON.stringify(obj2)); // { "a": 2, "b": { "c": 0}}
//
//     obj2.b.c = 3;
//     console.log(JSON.stringify(obj1)); // { "a": 1, "b": { "c": 3}}
//     console.log(JSON.stringify(obj2)); // { "a": 2, "b": { "c": 3}}

    // Deep Clone no functions
    // obj1 = { a: 0 , b: { c: 0}, d:function (){return 2+2}};
    // let obj3 = JSON.parse(JSON.stringify(obj1));
    // obj1.a = 4;
    // obj1.b.c = 4;
    // obj1.d = function (){return 3+3}
    // console.log(obj3); // { "a": 0, "b": { "c": 0}}
    // console.log(obj1);
    // console.log(obj1.d());

// }

// test();
//
// const target = {};
// const source = { b: 4, c: 5 , kur:function(){return 1}};
// Object.assign(target, source);
//
// console.log(target);
// // expected output: Object { a: 1, b: 4, c: 5 }
// console.log(source);

const target = {};
const source = { b: 4, c: 5 , kur:function(){return 1}, d:[1,2,3]};
Object.assign(target, source);
source.b = 16
console.log(source.kur())
source.kur = function (){return 16}
console.log(source.kur())
target.b = 64
target.d.push(2)
console.log(Object.is(target.d,source.d))



// console.log(target);
// console.log(target.kur())
// target.kur = function (){return 22}
// console.log(target.kur());
// console.log(source.kur())
// // expected output: Object { a: 1, b: 4, c: 5 }
// console.log(source);
// console.log(target)
