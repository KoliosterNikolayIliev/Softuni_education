import {html} from '../lib.js'
import {getItemId} from '../api/data.js';

let detailsTemplate = (item, isOwner) => html`
    <section id="details-page" class="content details">
        <h1>${item.title}</h1>

        <div class="details-content">
            <strong>Published in category ${item.category}</strong>
            <p>${item.content}</p>

            <div class="buttons">
                ${isOwner?html`<a href="/delete/${item._id}" class="btn delete">Delete</a>`:html``}
                ${isOwner?html`<a href="/edit/${item._id}" class="btn edit">Edit</a>`:html``}
                <a href="/" class="btn edit">Back</a>
            </div>
        </div>
    </section>`;


export async function detailsPage(context) {
    let id = context.params.id;
    let userId = sessionStorage.getItem('userId');
    let item = await getItemId(id);
    context.render(detailsTemplate(item, item._ownerId == userId));
}


