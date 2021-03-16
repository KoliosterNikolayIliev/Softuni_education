import {html, render} from 'https://unpkg.com/lit-html?module';


let select = (list) => html`
    <select id="menu">
        ${list.map(el => html`
            <option value=${el.id}>${el.text}</option>`)}
    </select>
`;

let main = document.getElementsByTagName('div')[0];
let endpoint = 'http://localhost:3030/jsonstore/advanced/dropdown';
let input = document.getElementById('itemText');
init();

async function init() {
    document.querySelector('form').addEventListener('submit', (event) => addItem(event,list));
    let response = await fetch(endpoint);
    let data = await response.json();
    let list = Object.values(data);

    update(list);
}

function update(list) {
    let result = select(list);
    render(result, main);
}

async function addItem(event,list) {
    event.preventDefault()
    let item = {
        text: input.value
    };
    let response = await fetch(endpoint, {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(item)
    });
    let result = await response.json();
    list.push(result);

    update(list);
    input.value=''
}