import {html} from '../../lib.js'
export let itemTemplate = (item) => html`
    <div class="card mb-4">
        <img class="card-img-top" src="${item.img}"
             alt="Card image cap" width="400">
        <div class="card-body">
            <h4 class="card-title">${item.title}</h4>
        </div>
        <div class="card-footer">
            <a href="/details/${item._id}">
                <button type="button" class="btn btn-info">Details</button>
            </a>
        </div>

    </div>`;