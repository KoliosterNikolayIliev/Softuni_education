import {html} from '../lib.js'
import {getItemId} from '../api/data.js';

let detailsTemplate = (item, isOwner) => html`
    `;


export async function detailsPage(context) {
    console.log('details');
    // let id = context.params.id;
    // let userId = sessionStorage.getItem('userId');
    // let item = await getItemId(id);
    // context.render(detailsTemplate(item, item._ownerId == userId));
}


