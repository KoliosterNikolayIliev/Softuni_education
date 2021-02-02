function attachEventsListeners() {

    let days = document.getElementById('days')
    let hours = document.getElementById('hours')
    let minutes = document.getElementById('minutes')
    let seconds = document.getElementById('seconds')

    document.getElementById('daysBtn').addEventListener('click',function (){convert(Number(days.value)*86400)})
    document.getElementById('hoursBtn').addEventListener('click',function (){convert(Number(hours.value)*3600)})
    document.getElementById('minutesBtn').addEventListener('click',function (){convert(Number(minutes.value)*60)})
    document.getElementById('secondsBtn').addEventListener('click',function (){convert(Number(seconds.value))})

    function convert (sec){
        let day = sec/(24*60*60);
        let hour = sec/(60*60);
        let minute = sec / 60;

        days.value = day;
        hours.value = hour;
        minutes.value = minute;
        seconds.value = sec;
    }
}
