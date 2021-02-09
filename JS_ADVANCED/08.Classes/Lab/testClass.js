class Person {
    constructor(name, age, job) {
        this.name = name;
        this.age = age;
        this.job = job;
    }

    makeBlowjob() {
        let blowjobType;
        if (this.job == 'programmer') {
            blowjobType = 'wonderful';
        } else {
            blowjobType = 'relatively good';
        }
        return `${this.name} is ${this.age} old and as a ${this.job} makes ${blowjobType} blowjobs !`;
    };
    static makeNice(){
        return 'hi'
    }

}

class Dickhead {
    constructor() {
        this.name = 'Pesho';
    }
}

newDick = new Dickhead();
otherDickhead = {name: 'Pesho'};

person = new Person('Pesho', 25, 'programmer');
console.log(person);
console.log(person.makeBlowjob());
person2 = new Person('Toshko', 18, 'junior developer');
console.log(person2.makeBlowjob());

console.log(newDick instanceof Dickhead);
console.log(Dickhead.makeNice);