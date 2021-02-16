function result() {
    const TASKS = {}
    class Employee {
        constructor(name, age) {
            if (new.target === Employee) {
                throw new Error('Cannot instantiate directly');
            }
            this.name = name;
            this.age = age;
            this.salary = 0;
            this.tasks = [];
        }

        work() {
            let currentTask = this.tasks.shift();
            console.log(this.name + currentTask);
            this.tasks.push(currentTask);
        }

        collectSalary() {
            console.log(`${this.name} received ${this.getSalary()} this month.`);
        }

        getSalary() {
            return this.salary;
        }
    }

    class Junior extends Employee {
        constructor(name, age) {
            super(name, age);
            this.tasks.push(' is working on a simple task.');
        }
    }

    class Senior extends Employee {
        constructor(name, age) {
            super(name, age);
            this.tasks.push(' is working on a complicated task.');
            this.tasks.push(' is taking time off work.');
            this.tasks.push(' is supervising junior workers.');

        }
    }

    class Manager extends Employee {
        constructor(name, age) {
            super(name, age);
            this.dividend = 0;
            this.tasks.push(' scheduled a meeting.');
            this.tasks.push(' is preparing a quarterly report.');
        }

        getSalary() {
            return this.salary + this.dividend;
        }
    }

    return {Employee, Junior, Senior, Manager};
}

let {expect} = require('chai')

result = result();

var guy1 = new result.Junior('dragan', 23);
var guy1parent = Object.getPrototypeOf(Object.getPrototypeOf(guy1));
var guy2 = new result.Senior('petkan', 24);
var guy2parent = Object.getPrototypeOf(Object.getPrototypeOf(guy2));
var guy3 = new result.Manager('bojan', 25);
var guy3parent = Object.getPrototypeOf(Object.getPrototypeOf(guy3));

expect(guy1parent === Object.prototype).to.equal(false, "Prototype chain was broken from Junior.");
expect(guy2parent === Object.prototype).to.equal(false, "Prototype chain was broken from Senior.");
expect(guy3parent === Object.prototype).to.equal(false, "Prototype chain was broken from Manager.");

expect(guy1parent === guy2parent).to.equal(true, "Junior and Senior aren't related (parent class not the same).");
expect(guy2parent === guy3parent).to.equal(true, "Senior and Manager aren't related (parent class not the same).");
expect(guy1parent === guy3parent).to.equal(true, "Junior and Manager aren't related (parent class not the same).");

expect(guy1.salary).to.equal(0, "Salary not initialized trough constructor on Junior.");
guy1.salary = 1000;
expect(guy1.salary).to.equal(1000, "Salary could not be changed at runtime on Junior.");

expect(guy2.salary).to.equal(0, "Salary not initialized trough constructor on Senior.");
guy2.salary = 2000;
expect(guy2.salary).to.equal(2000, "Salary could not be changed at runtime on Senior.");

expect(guy3.salary).to.equal(0, "Salary not initialized trough constructor on Manager.");
expect(guy3.dividend).to.equal(0, "Dividend not initialized trough constructor on Manager.");
guy3.salary = 3000;
guy3.dividend = 500;
expect(guy3.salary).to.equal(3000, "Salary could not be changed at runtime on Manager.");
expect(guy3.dividend).to.equal(500, "Dividend could not be changed at runtime on Manager.");

