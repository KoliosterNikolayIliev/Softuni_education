// function add(num) {
//     let sum = num;
//
//     function calc(num2) {
//         sum += num2;
//         return calc;
//     }
//
//     calc.toString = function() { return sum };
//     return calc;
// }

// let add = (function () {
//     let total = 0;
//     return function sum(a) {
//         total += a;
//         sum.toString = () => total;
//         return sum;
//     }
// })();
//
// console.log(add(1));
// console.log(add(1)(6)(-3));

// let f = (function () {
//     let total = 0;
//     return function sum(a) {
//         total += a;
//         sum.toString = () => total;
//         return sum;
//     }
// })();
//
// console.log(f(6)(7));

// function add(a) {
//     let sum = a
//
//     function add_and_repeat(b) {
//         if(b){
//             sum += b
//             return add_and_repeat
//         }
//         else
//             return sum;
//     }
//
//     add_and_repeat.toString = function() { return sum }
//
//     return add_and_repeat
// }

// function add(a){
//     let sum =0;
//     sum+=a;
//
//     function calc(b){
//         sum+=b;
//         return calc;
//     }
//     calc.toString = () => sum;
//     return calc;
// }
//
// console.log(add(1));
// console.log(add(1)(6)(-3));
//
// function a(){
//     function b(){}
//     b.toString = () =>5
//     return function b(){};
// }

// function add() {
//     let slice = Array.prototype.slice,
//         sum = 0,
//         closure = function() {
//             let cargs = slice.call(arguments);
//             for (let i = 0, l = cargs.length; i < l; i++) {
//                 sum += cargs[i]*1;
//             }
//             return cargs.length ? closure : sum;
//         };
//     return closure.apply(null, slice.call(arguments));
// }
//
// console.log(add(1,2,7)(5)(4)(2,3)('3.14',2.86)); // function
// console.log(add(1,2,7)(5)(4)(2,3)('3.14',2.86)()); // 30

function add(a) {
    let sum = 0;
    sum += a;

    function calc(b) {
        sum += b;
        console.log(calc);
        return calc;
    }

    console.log(calc.toString );
    calc.toString = function (){return sum};
    console.log(calc);
    return calc;
}

console.log(add(1).toString());
console.log(add(1)(6)(-3).toString());