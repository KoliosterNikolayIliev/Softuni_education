import {html} from '../lib.js'
import {getItemId} from '../api/data.js';

let detailsTemplate = (item, isOwner) => html`
    <div class="container home some">
        <img class="det-img" src="${item.img}" />
        <div class="desc">
            <h2 class="display-5">${item.title}</h2>
            <p class="infoType">Description:</p>
            <p class="idea-description">${item.description}</p>
        </div>
        
        ${isOwner?html`<div class="text-center">
            <a class="btn detb" href="/delete/${item._id}">Delete</a>
        </div>`:''}
    </div>`;


export async function detailsPage(context) {
    let id = context.params.id;
    let userId = sessionStorage.getItem('userId');
    let item = await getItemId(id);
    context.render(detailsTemplate(item, item._ownerId == userId));
}


