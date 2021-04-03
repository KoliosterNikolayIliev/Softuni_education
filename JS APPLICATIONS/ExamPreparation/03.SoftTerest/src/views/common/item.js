import {html} from '../../lib.js'
export let itemTemplate = (item) => html`
    <div class="card overflow-hidden current-card details" style="width: 20rem; height: 18rem;">
        <div class="card-body">
            <p class="card-text">${item.title}</p>
        </div>
        <img class="card-image" src="${item.img}" alt="Card image cap">
        <a class="btn" href="/details/${item._id}">Details</a>
    </div>`;