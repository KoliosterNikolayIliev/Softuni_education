function solve(){
    let movieName = document.querySelector('*[placeholder="Name"]')
    let hall = document.querySelector('*[placeholder="Hall"]')
    let ticketPrice = document.querySelector('*[placeholder="Ticket Price"]')
    let buttonOnscreen = document.getElementsByTagName('button')[0]
    let clearButton = document.getElementsByTagName('button')[1]
    let sectionMoviesUl = document.getElementById('movies').children[1]
    let archiveUl = document.getElementById('archive').children[1]

    buttonOnscreen.addEventListener('click', addMovie)
    clearButton.addEventListener('click', clearArchive)

    function addMovie(event){
        event.preventDefault()
        let tPrice = Number(ticketPrice.value)

        if (movieName.value!==''&& hall.value!==''&& typeof tPrice==='number'){
            createMovie()
        }
    }
    function createMovie(){
        let li = document.createElement('li')
        let span = document.createElement('span')
        span.textContent = movieName.value
        let strong = document.createElement('strong')
        strong.textContent = hall.value
        let div = document.createElement('div')
        let strong2 = document.createElement('strong')
        strong2.textContent = Number(ticketPrice.value).toFixed(2)
        let input = document.createElement('input')
        input.placeholder = 'Tickets Sold'
        let arcButt = document.createElement('button')
        arcButt.textContent = 'Archive'
        arcButt.addEventListener('click', move)
        div.appendChild(strong2)
        div.appendChild(input)
        div.appendChild(arcButt)
        li.appendChild(span)
        li.appendChild(strong)
        li.appendChild(div)
        sectionMoviesUl.appendChild(li)
        function move(){
            sectionMoviesUl.removeChild(li)
            let newLi = document.createElement('li')
            let newSpan = document.createElement('span')
            newSpan.textContent = span.textContent
            let newStrong = document.createElement('strong')
            newStrong.textContent = 'Total amount: '+(Number(strong2.textContent)*Number(input.value)).toFixed(2)
            let delBtn = document.createElement('button')
            delBtn.textContent = 'Delete'
            delBtn.addEventListener('click', del)
            newLi.appendChild(newSpan)
            newLi.appendChild(newStrong)
            newLi.appendChild(delBtn)
            archiveUl.appendChild(newLi)
            function del(){archiveUl.removeChild(newLi)}
        }
    }


    function clearArchive(event){
        event.preventDefault()
        let emptyUl = document.createElement('ul')
        document.getElementById('archive').replaceChild(emptyUl,archiveUl)
    }
}
let{expect}=require('chai')
//Zero Test - Add
document.body.innerHTML = `<h1>Central Cinema</h1>
    <form id="add-new">
        <h2>Add Movie</h2>
        <div id='container'>
            <input type="text" placeholder="Name" />
            <input type="text" placeholder="Hall" />
            <input type="text" placeholder="Ticket Price" />
            <button>On Screen</button>
        </div>
    </form>
    <section id="movies">
        <h2>Movies on Screen</h2>
        <ul></ul>
    </section>
    <section id="archive">
        <h2>Аrchive</h2>
        <ul></ul>
        <button>Clear</button>
    </section>
    <script>document.onload = solve();</script>`;


result();

const form = document.getElementById('container');
let [name, hall, price, addBtn] = Array.from(form.children);

name.value = 'Avengers: Endgame';
hall.value = 'Main';
price.value = '12.00';


addBtn.click();
let newLiItem = Array.from(document.querySelector("#movies > ul").children)[0];
let insideLiElements = Array.from(newLiItem.children); // [span, strong, div]
let [liName, liHall, liDiv] = insideLiElements;
let [liPrice, liCount, btnArh] = Array.from(liDiv.children); // [strong, input, btn]
liCount.value = 2;
addBtn.click();

// Add new Movie, check structure;
expect(insideLiElements.length).to.be.equal(3,'New list item has invalid structure');

expect(liName.tagName).to.be.equal("SPAN", 'Movie name element should be SPAN');
expect(liHall.tagName).to.be.equal("STRONG", 'Movie hall element should be STRONG');
expect(liDiv.tagName).to.be.equal("DIV", 'Movie must contain div element');
expect(liPrice.tagName).to.be.equal("STRONG", 'Movie price element should be STRONG');
expect(liCount.tagName).to.be.equal("INPUT", 'Movie price element should be INPUT');
expect(btnArh.tagName).to.be.equal("BUTTON", 'Archive button element should be BUTTON');

expect(liName.textContent).to.be.equal("Avengers: Endgame", 'Movie name should be Avengers: Endgame');
expect(liHall.textContent).to.be.equal("Hall: Main", 'Movie hall should be Main');
expect(liPrice.textContent).to.be.equal("12.00", 'Movie price should be 12.00');
expect(btnArh.textContent).to.be.equal("Archive", 'Archive button name should be Archive');