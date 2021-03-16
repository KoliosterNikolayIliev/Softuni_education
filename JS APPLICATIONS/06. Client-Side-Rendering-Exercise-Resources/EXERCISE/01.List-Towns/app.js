import {html, render} from 'https://unpkg.com/lit-html?module';

let listTemplate = (data) => html`
    <ul>
        ${data.map(el => html`
            <li>${el}</li>`)}
    </ul>`;

document.getElementById('btnLoadTowns').addEventListener('click', update);

function update(event) {
    event.preventDefault()
    let towns = document.getElementById('towns').value.split(',').map(x => x.trim());
    let result = listTemplate(towns);
    let root = document.getElementById('root');
    render(result, root);
}