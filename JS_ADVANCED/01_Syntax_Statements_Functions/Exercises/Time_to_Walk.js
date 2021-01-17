function walkingTime(steps, footPrint, speed){
    footPrint = footPrint/1000;
    let distance = steps*footPrint;
    let breaks = Math.floor(distance/0.5);
    let time = distance/speed;
    let hours = Math.floor(time/60).toString();
    let minutes = Math.floor(time*60 % 60 + breaks).toString();
    let seconds = Math.round((time*60 % 60 - Math.floor(time*60 % 60))*60).toString();

    if (hours.length<2){
        hours='0'+hours;
    }
    if (minutes.length<2){
        minutes='0'+minutes;
    }
    if (seconds.length<2){
        seconds='0'+seconds;
    }

    console.log(`${hours}:${minutes}:${seconds}`)
}

walkingTime(4000, 0.60, 5)
walkingTime(2564, 0.70, 5.5)