import {html, render} from 'https://unpkg.com/lit-html?module';


let row = (student, select) => html`
    <tr class=${select ? 'select' : ''}>
        <td>${student.firstName} ${student.lastName}</td>
        <td>${student.email}</td>
        <td>${student.course}</td>
    </tr>`;

let tbody = document.getElementsByTagName('tbody')[0];
let input = document.getElementById('searchField');
start();

async function start() {
    document.getElementById('searchBtn').addEventListener('click', search);
    let url = 'http://localhost:3030/jsonstore/advanced/table';
    let data = await (await fetch(url)).json();
    let list = Object.values(data);

    function search() {
        update(list, input.value);
    }

    update(list);
}

function update(list, match = '') {
    let result = list.map(s => row(s, compare(s, match)));
    render(result, tbody);
    input.value = '';
}

function compare(item, match) {
    return Object.values(item).some(value => match && value.toLowerCase().includes(match));
}