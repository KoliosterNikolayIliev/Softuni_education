import {towns} from './towns.js';
import {html, render} from 'https://unpkg.com/lit-html?module';


let counter = 0
let templateSearch = (towns, match) => html`
    <article>
        <div id="towns">
            <ul>
                ${towns.map(t => templateItem(t, match))}
            </ul>
        </div>
        <input type="text" id="searchText"/>
        <button @click="${search}">Search</button>
        <div id="result" style="display: ${counter>0?'':'none'}">${counter} matches found</div>
    </article>
`;

let templateItem = function (name, match) {
    let temp = html`
    <li class=${(match && name.toLowerCase().includes(match.toLowerCase())) ? 'active' : ''}>${name}</li>
`;

    if (temp.values[0]=='active'){
        counter++
    }
    return temp
}

let main = document.body;
update();


function update(match = '') {
    let result = templateSearch(towns, match);
    render(result, main);

}

function search() {
    let match = document.getElementById('searchText');
    counter=0
    update(match.value);
    // match.value=''
}
