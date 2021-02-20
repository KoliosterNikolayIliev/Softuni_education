function solve() {
    let movieName = document.querySelector('*[placeholder="Name"]');
    let hall = document.querySelector('*[placeholder="Hall"]');
    let ticketPrice = document.querySelector('*[placeholder="Ticket Price"]');
    let buttonOnscreen = document.getElementsByTagName('button')[0];
    let clearButton = document.getElementsByTagName('button')[1];
    let sectionMoviesUl = document.getElementById('movies').children[1];
    let archiveUl = document.getElementById('archive').children[1];

    document.getElementsByTagName('body')[0].addEventListener('click', action);

    function action(event) {
        if (event.target === buttonOnscreen) {
            event.preventDefault();
            if (!isNaN(Number(ticketPrice.value)) && movieName.value !== '' && hall.value !== '' && ticketPrice.value !== '') {
                appendLine(createLine());
            }
        }
        if (event.target.textContent === 'Archive') {
            move(event.target)
        }
        if (event.target.textContent==='Delete'){
            archiveUl.removeChild(event.target.parentElement)
        }
        if (event.target.textContent==='Clear'){
            let ul = createEl('ul')
            archiveUl.parentElement.replaceChild(ul,archiveUl)
        }


    }
    function move(button){
        let div = button.parentElement
        let li = button.parentElement.parentElement
        if (!isNaN(Number(div.children[1].value))&&div.children[1].value!==''){
            sectionMoviesUl.removeChild(li)
            li.removeChild(div)
            li.children[1].textContent = 'Total amount:'+' '+(Number(div.children[0].textContent)*Number(div.children[1].value)).toFixed(2)
            let but = createEl('button', 'Delete')
            li.appendChild(but)
            archiveUl.appendChild(li)
        }

    }

    function createLine() {
        let li = createEl('li');
        let span = createEl('span', movieName.value);
        let strong = createEl('strong', hall.value);
        let div = createEl('div');
        let divStr = createEl('strong',Number(ticketPrice.value).toFixed(2));
        let input = createEl('input');
        input.placeholder = 'Tickets Sold';
        let button = createEl('button', 'Archive');
        let result = [li, span, strong, div, divStr, input, button];
        return result;
    }

    function appendLine(list) {
        list[0].appendChild(list[1]);
        list[0].appendChild(list[2]);
        list[3].appendChild(list[4]);
        list[3].appendChild(list[5]);
        list[3].appendChild(list[6]);
        list[0].appendChild(list[3]);
        movieName.value = ''
        hall.value = ''
        ticketPrice.value = ''
        sectionMoviesUl.appendChild(list[0]);
    }

    function createEl(type, content, className) {
        const result = document.createElement(type);
        if (content) {
            result.textContent = content;
        }
        if (className) {
            result.className = className;
        }
        return result;
    }
}
