class Bank {
    constructor(bankName) {
        this._bankName = bankName;
        this.allCustomers = [];
        this.transactions = [];
    }

    newCustomer(customer) {
        if (this.allCustomers.find(c => c.personalId === customer.personalId) !== undefined) {
            throw new Error(`${customer.firstName} ${customer.lastName} is already our customer!`);
        }
        customer.transactionsNumber = 0
        this.allCustomers.push(customer);
        return customer;
    }

    depositMoney(personalId, amount) {
        let customer = this.allCustomers.find(c => c.personalId === personalId);
        if (customer === undefined) {
            throw new Error('We have no customer with this ID!');
        }
        if (!customer.hasOwnProperty('totalMoney')) {
            customer.totalMoney = 0;
        }
        if (!customer.hasOwnProperty('transactions')) {
            customer.transactions = [];
        }
        customer.totalMoney += amount;
        customer.transactionsNumber+=1
        let transaction = {type:'made deposit of', amount:amount, number:customer.transactionsNumber}
        customer.transactions.push(transaction)
        return `${customer.totalMoney}$`;

    }

    withdrawMoney(personalId, amount) {
        let customer = this.allCustomers.find(c => c.personalId === personalId);
        if (customer === undefined) {
            throw new Error('We have no customer with this ID!');
        }
        if (!customer.hasOwnProperty('totalMoney')) {
            customer.totalMoney = 0;
        }
        if (customer.totalMoney < amount) {
            throw new Error(`${customer.firstName} ${customer.lastName} does not have enough money to withdraw that amount!`);
        }
        if (!customer.hasOwnProperty('transactions')) {
            customer.transactions = [];
        }
        customer.totalMoney -= amount;
        customer.transactionsNumber+=1
        let transaction = {type:'withdrew', amount:amount,number:customer.transactionsNumber}
        customer.transactions.push(transaction)

        return `${customer.totalMoney}$`;

    }

    customerInfo(personalId) {
        let customer = this.allCustomers.find(c => c.personalId === personalId);
        if (customer === undefined) {
            throw new Error('We have no customer with this ID!');
        }
        customer.transactions = customer.transactions.sort((a,b)=>b.number-a.number)
        let result = [`Bank name: ${this._bankName}`,`Customer name: ${customer.firstName} ${customer.lastName}`,`Customer ID: ${customer.personalId}`,`Total Money: ${customer.totalMoney}$`,'Transactions:']
        for (let i = 0; i < customer.transactions.length; i++) {
            result.push(`${customer.transactions[i].number}. ${customer.firstName} ${customer.lastName} ${customer.transactions[i].type} ${customer.transactions[i].amount}$!`)
        }
        return result.join('\n')
    }
}

// let bank = new Bank('pesho');
// console.log(bank.newCustomer({firstName: 'goro', lastName: 'gorov', personalId: 12}));
// // console.log(bank.newCustomer({firstName:'gogo', lastName:'gogov', personalId:13}));
// // console.log(bank.depositMoney(12,100))
// // console.log(bank.depositMoney(12,100))
// console.log(bank.withdrawMoney(13, 100));


let bank = new Bank('SoftUni Bank');

console.log(bank.newCustomer({firstName: 'Svetlin', lastName: 'Nakov', personalId: 6233267}));
console.log(bank.newCustomer({firstName: 'Mihaela', lastName: 'Mileva', personalId: 4151596}));

bank.depositMoney(6233267, 250);
console.log(bank.depositMoney(6233267, 250));
bank.depositMoney(4151596,555);

console.log(bank.withdrawMoney(6233267, 125));

console.log(bank.customerInfo(6233267));


