function dayWeek (day) {
    let daysInWeek = {'Sunday':7, 'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6};
    if (day in daysInWeek){
        console.log(daysInWeek[day])
    } else {
        console.log('error')
    }
}

dayWeek('Monday')
dayWeek('Friday')
dayWeek('Invalid')