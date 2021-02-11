function solve(tickets, filtering){
    console.log(tickets);
    tickets = tickets.forEach(item => {item.split('|')})
    // function splitting(element){
    //     return element.split('|')
    // }
    return tickets
}

console.log(solve(['Philadelphia|94.20|available',
        'New York City|95.99|available',
        'New York City|95.99|sold',
        'Boston|126.20|departed'],
    'destination'
));

console.log(solve(['Philadelphia|94.20|available',
        'New York City|95.99|available',
        'New York City|95.99|sold',
        'Boston|126.20|departed'],
    'status'
));

