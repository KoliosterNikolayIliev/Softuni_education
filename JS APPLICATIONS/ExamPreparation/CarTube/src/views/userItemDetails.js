import {html} from '../lib.js'

import {getUserItems} from '../api/data.js';
import {itemTemplate} from './common/item.js';

let myTemplate = (data) => html`
    <section id="my-listings">
        <h1>My car listings</h1>
        <div class="listings">
            ${data.length > 0 ? data.map(item => itemTemplate(item)) : html`<p class="no-cars"> You haven't listed any cars yet.</p>`}
        </div>
    </section>`;



export async function userItemsPage(context) {
    let data = await getUserItems()
    context.render(myTemplate(data))
}