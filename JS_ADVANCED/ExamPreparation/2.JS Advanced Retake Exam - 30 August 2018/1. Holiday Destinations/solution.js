function addDestination() {
    let city = document.getElementsByClassName('inputData')[0];
    let country = document.getElementsByClassName('inputData')[1];
    let selector = document.getElementById('seasons');
    let table = document.getElementById('destinationsList');
    let seasons = {
        summer: document.getElementById('summer'),
        autumn: document.getElementById('autumn'),
        winter: document.getElementById('winter'),
        spring: document.getElementById('spring')
    };
    if (city.value !== '' && country.value !== '') {
        let tr = document.createElement('tr');
        let destination = document.createElement('td');
        let tdSeason = document.createElement('td');
        destination.textContent = city.value + ', ' + country.value;
        tdSeason.textContent = selector.value.charAt(0).toUpperCase() + selector.value.slice(1);
        tr.appendChild(destination);
        tr.appendChild(tdSeason);
        table.appendChild(tr);
        city.value = ''
        country.value = ''
        seasonValue(selector.value);
    }

    function seasonValue(season) {
        seasons[season].value = Number(seasons[season].value) + 1;
    }
}
