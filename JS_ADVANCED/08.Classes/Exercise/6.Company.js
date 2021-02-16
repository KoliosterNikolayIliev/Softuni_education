class Company {
    constructor() {
        this.departments = [];
    }

    addEmployee(name, salary, position, department) {
        let data = [name, salary, position, department];
        let message = 'Invalid input!';
        if (data[1] < 0) {
            throw new Error(message);
        }
        for (const item of data) {
            if (item === '' || item === null || item === undefined) {
                throw new Error(message);
            }
        }
        let pushed = false;
        let employee = {name: name, salary: salary, position: position};
        if (this.departments.length > 0) {
            for (let dept of this.departments) {
                if (Object.keys(dept)[0].toString() === department) {
                    dept[department].push(employee);
                    dept['totalSalary'] += employee.salary;
                    pushed = true;
                }
            }
        }
        if (pushed === false) {
            let newDept = {};
            newDept[department] = [];
            newDept['totalSalary'] = 0;
            newDept['averageSalary'] = 0;
            newDept['totalSalary'] += employee.salary;
            newDept[department].push(employee);
            this.departments.push(newDept);
        }
        return `New employee is hired. Name: ${name}. Position: ${position}`;
    }

    bestDepartment() {
        let salaryArr = [];
        for (const department of this.departments) {
            department.averageSalary = (department.totalSalary / Object.values(department)[0].length).toFixed(2);
            salaryArr.push([Object.keys(department)[0], department.averageSalary]);
        }
        salaryArr.sort(function (b, a) {
            return Number(a[1]) - Number(b[1]);
        });
        let bestDept;
        for (const department of this.departments) {
            if (Object.keys(department)[0].toString() === salaryArr[0][0])
                bestDept = department;
        }
        bestDept[Object.keys(bestDept)[0]] = bestDept[Object.keys(bestDept)[0]].sort(function (a, b) {
            if (a.name === b.name) {
                // Price is only important when cities are the same
                return b.name - a.name;
            }
            return a.salary < b.salary ? 1 : -1;
        });
        let result = `Best Department is: ${Object.keys(bestDept)[0].toString()}\nAverage salary: ${bestDept.averageSalary}`;
        for (let user of Object.values(bestDept)[0]) {
            result += `\n${user.name} ${user.salary} ${user.position}`;
        }
        return result;
    }
}

let c = new Company();
c.addEmployee("Stanimir", 2000, "engineer", "Construction");
c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
c.addEmployee("Slavi", 500, "dyer", "Construction");
c.addEmployee("Stan", 2000, "architect", "Construction");
c.addEmployee("Stanimir", 1200, "digital marketing manager", "Marketing");
c.addEmployee("Pesho", 1000, "graphical designer", "Marketing");
c.addEmployee("Gosho", 1350, "HR", "Human resources");
console.log(c.bestDepartment());
// console.log(c.departments);
