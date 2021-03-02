let forecastDiv = document.getElementById('forecast')
let divCurrent = document.getElementById('current')
let divUpcoming = document.getElementById('upcoming')
let divCurLabel = document.getElementsByClassName('label')[0]
let divUpLabel = document.getElementsByClassName('label')[1]
function attachEvents() {
    document.getElementById('submit').addEventListener('click', getWeather);

}

attachEvents();

async function getWeather() {
    divUpcoming.innerHTML = ''
    divCurrent.innerHTML = ''
    let input = document.getElementById('location');
    let cityName = input.value;

    let code = await getCode(cityName);
    let currentUrl = 'http://localhost:3030/jsonstore/forecaster/today/';
    let upcomingUrl = 'http://localhost:3030/jsonstore/forecaster/upcoming/';

    let [current, upcoming] = await Promise.all([getInfo(code, currentUrl), getInfo(code, upcomingUrl)]);

    input.value= ''
    console.log(upcoming);
    appendContent(current, upcoming)
}

async function getCode(cityName) {
    let url = 'http://localhost:3030/jsonstore/forecaster/locations';
    let response = await fetch(url);
    let data = await response.json();
    try{
        return data.find(x => x.name.toLowerCase() == cityName.toLowerCase()).code;
    }catch (error){
        forecastDiv.style.display = 'block'
        let spanError = createEl('span',Error,'Error', 'Error - wrong entry!')
        spanError.style.color = 'red'
        forecastDiv.children[0].appendChild(spanError)

    }

}

async function getInfo(code, inputUrl) {
    let url = inputUrl + code;
    let response = await fetch(url);
    let data = await response.json();
    return data;
}

function appendContent(current, upcoming){
    let weatherIcons = {
        'Sunny': '&#x2600;',
        'Partly sunny': '&#x26C5;',
        'Overcast': '&#x2601;',
        'Rain': '&#x2614;',
        'Degrees': '&#176;',
    };
    forecastDiv.style.display = 'block'
    divCurrent.appendChild(divCurLabel)
    divUpcoming.appendChild(divUpLabel)
    let divForecasts = createEl('div','forecasts')
    divCurrent.appendChild(divForecasts)
    let spanCondSymbol = createEl('span','condition symbol','',weatherIcons[current.forecast.condition])
    divForecasts.appendChild(spanCondSymbol)
    let spanCondition = createEl('span','condition')
    divForecasts.appendChild(spanCondition)
    let spanCity = createEl('span','forecast-data', '', current.name)
    spanCondition.appendChild(spanCity)
    let spanDeg = createEl('span','forecast-data', '', `${current.forecast.low}${weatherIcons['Degrees']}/${current.forecast.high}${weatherIcons['Degrees']}`)
    spanCondition.appendChild(spanDeg)
    let spanWeather = createEl('span','forecast-data', '', current.forecast.condition)
    spanCondition.appendChild(spanWeather)


    let divForecastInfo = createEl('div','forecast-info')
    divUpcoming.appendChild(divForecastInfo)
    for (let i = 0; i < upcoming.forecast.length; i++) {
        let spanUpcoming = createEl('span', 'upcoming')
        divForecastInfo.appendChild(spanUpcoming)
        let spanSymbol = createEl('span', 'symbol', '', weatherIcons[upcoming.forecast[i].condition])
        spanUpcoming.appendChild(spanSymbol)
        let spanDegU = createEl('span','forecast-data', '', `${upcoming.forecast[i].low}${weatherIcons['Degrees']}/${upcoming.forecast[i].high}${weatherIcons['Degrees']}`)
        spanUpcoming.appendChild(spanDegU)
        let spanWeatherUp = createEl('span','forecast-data', '', upcoming.forecast[i].condition)
        spanUpcoming.appendChild(spanWeatherUp)
    }

}

function createEl(type,elClass, id, content){
    let el = document.createElement(type)
    if (elClass){el.className = elClass}
    if (id){el.id = id}
    if (content){el.innerHTML = content}
    return el
}


