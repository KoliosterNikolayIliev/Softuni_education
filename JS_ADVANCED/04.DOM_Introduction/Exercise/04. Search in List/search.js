function search() {
    let searchedItem = document.getElementById('searchText').value
    let cities = document.querySelectorAll('#towns>li')
    let matchCounter = 0
    for (const city of cities) {
        if (city.textContent.includes(searchedItem)){
            city.style.fontWeight = 'bold'
            city.style.textDecoration = 'underline'
            matchCounter++
            document.getElementById('result').textContent = `${matchCounter} matches found`
        }
    }
}
