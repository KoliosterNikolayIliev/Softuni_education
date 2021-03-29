import {html} from '../../lib.js'
export let itemTemplate = (item) => html`
    <div class="meme">
        <div class="card">
            <div class="info">
                <p class="meme-title">${item.title}</p>
                <img class="meme-image" alt="meme-img" src="${item.imageUrl}">
            </div>
            <div id="data-buttons">
                <a class="button" href="/details/${item._id}">Details</a>
            </div>
        </div>
    </div>`;


