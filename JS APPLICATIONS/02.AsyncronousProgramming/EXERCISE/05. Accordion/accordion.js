let main = document.getElementById('main')
function solution(){
    getArticles()
}
solution()
async function getArticles(){
    let url = 'http://localhost:3030/jsonstore/advanced/articles/list'
    let response = await fetch(url)
    let data = await response.json()
    for (const item of data) {
        let divAccordion = createEl('div','accordion')
        main.appendChild(divAccordion)
        let divHead = createEl('div','head')
        divAccordion.appendChild(divHead)
        let span = createEl('span', '','', item.title)
        divHead.appendChild(span)
        let button = createEl('button', 'button', item._id,'More')
        button.addEventListener('click',showHide)
        divHead.appendChild(button)
        let divExtra = createEl('div', 'extra')
        divAccordion.appendChild(divExtra)
        let p = createEl('p')
        divExtra.appendChild(p)
        p.innerHTML = (await getInfo(item._id)).content
    }
}

function showHide(event){
    let button = event.target
    let div = button.parentElement.nextSibling
    if (button.innerHTML =='More'){
        div.style.display = 'block'
        button.innerHTML = 'Less'
    }else {
        div.style.display = 'none'
        button.innerHTML = 'More'
    }
}

function createEl(type,elClass, id, content){
    let el = document.createElement(type)
    if (elClass){el.className = elClass}
    if (id){el.id = id}
    if (content){el.innerHTML = content}
    return el
}

async function getInfo(id) {
    let url = 'http://localhost:3030/jsonstore/advanced/articles/details/'+id
    let response = await fetch(url);
    let text = await response.json();
    return text;
}