import {html, render} from 'https://unpkg.com/lit-html?module';
import {cats} from './catSeeder.js';


let catTemplate = (cat) => html`
    <li>
        <img src="./images/${cat.imageLocation}.jpg" width="250" height="250" alt="Card image cap">
        <div class="info">
            <button class="showBtn">Show status code</button>
            <div class="status" style="display: none" id=${cat.id}>
                <h4>Status Code: ${cat.statusCode}</h4>
                <p>${cat.statusMessage}</p>
            </div>
        </div>
    </li>`;


let main = document.getElementById('allCats');


let renderedCats = html`
    <ul @click=${toggle}>${cats.map(c => catTemplate(c))}</ul>`;
console.log(renderedCats);
render(renderedCats, main);

function toggle(event) {
    if (event.target.className === 'showBtn') {
        let div = event.target.parentNode.children[1];
        if (div.style.display === 'none') {
            div.removeAttribute('style');
        } else {
            div.style.display = 'none';
        }
    }
}