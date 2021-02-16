function solve(ticketsList, sortParam) {

    let tickets = [];

    class Ticket {
        constructor(destination, price, status) {
            this.destination = destination;
            this.price = Number(price);
            this.status = status;
        }
    }

    ticketsList.forEach((el, index, ticketsList) => {
        ticketsList[index] = el.split('|');
    });

    ticketsList.forEach((el) => {
        tickets.push(new Ticket(el[0], el[1], el[2]));
    });
    const sortMap = {
        'destination': (objA, objB) => {
            return objA.destination.localeCompare(objB.destination);
        },
        'price': (objA, objB) => {
            return objA.price - objB.price;
        },
        'status': (objA, objB) => {
            return objA.status.localeCompare(objB.status);
        },
    };
    tickets.sort(sortMap[sortParam]);

    return tickets;
}


console.log(solve(['Philadelphia|94.20|available',
        'New York City|95.99|available',
        'New York City|95.99|sold',
        'Boston|126.20|departed'],
    'destination'
));

// console.log(solve(['Philadelphia|94.20|available',
//         'New York City|95.99|available',
//         'New York City|95.99|sold',
//         'Boston|126.20|departed'],
//     'status'
// ));


