import {html} from '../lib.js'
import {getItemId} from '../api/data.js';

let detailsTemplate = (item, isOwner) => html`
    <section id="listing-details">
        <h1>Details</h1>
        <div class="details-info">
            <img src="${item.imageUrl}">
            <hr>
            <ul class="listing-props">
                <li><span>Brand:</span>${item.brand}</li>
                <li><span>Model:</span>${item.model}</li>
                <li><span>Year:</span>${item.year}</li>
                <li><span>Price:</span>${item.price}$</li>
            </ul>

            <p class="description-para">${item.description}</p>

            <div class="listings-buttons">
                ${isOwner?html`<a href="/edit/${item._id}" class="button-list">Edit</a>
                <a href="/delete/${item._id}" class="button-list">Delete</a>`:''}
                
            </div>
        </div>
    </section>`;


export async function detailsPage(context) {
    let id = context.params.id;
    let userId = sessionStorage.getItem('userId');
    let item = await getItemId(id);
    context.render(detailsTemplate(item, item._ownerId == userId));
}


