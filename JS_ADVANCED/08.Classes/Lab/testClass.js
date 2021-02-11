// class Person {
//     constructor(name, age, job) {
//         this.name = name;
//         this.age = age;
//         this.job = job;
//     }
//
//     makeBlowjob() {
//         let blowjobType;
//         if (this.job == 'programmer') {
//             blowjobType = 'wonderful';
//         } else {
//             blowjobType = 'relatively good';
//         }
//         return `${this.name} is ${this.age} old and as a ${this.job} makes ${blowjobType} blowjobs !`;
//     };
//     static makeNice(){
//         return 'hi'
//     }
//
// }
//
// class Dickhead {
//     constructor() {
//         this.name = 'Pesho';
//     }
// }
//
// newDick = new Dickhead();
// otherDickhead = {name: 'Pesho'};
//
// person = new Person('Pesho', 25, 'programmer');
// console.log(person);
// console.log(person.makeBlowjob());
// person2 = new Person('Toshko', 18, 'junior developer');
// console.log(person2.makeBlowjob());
//
// console.log(newDick instanceof Dickhead);
// console.log(Dickhead.makeNice);
//
// class Other {
//     static fuck() {
//         return 'fuckoff';
//     }
// }


class Person {
    age = 100;

    constructor(name, lastName) {
        this.name = name;
        this.lastName = lastName;
    }

    static fullName(a, b) {
        return a + b;
    }

    static fuckoff(c) {
        return this.fullName(person.name, person.lastName) + c + 'pesho';

    }
    sallary(){
        return 'milioni levove'
    }
}


let person = new Person('pesho', 'toshev');

console.log(Person.fullName(person.name, person.lastName));

console.log(person);

console.log(Person.fuckoff('Kurev'));

class Engineer extends Person {
    constructor(name, lastname, work) {
        super(name, lastname);
        this.work = work;
    }
}

engineer = new Engineer('Pesho', 'Peshev', 'ballscratching' )
engineer.fullName = Engineer.fullName(engineer.name, engineer.lastName)
console.log(engineer);
console.log(Engineer.fuckoff(engineer.work));
console.log(engineer.age);
console.log(person.sallary());
console.log(engineer.sallary());


