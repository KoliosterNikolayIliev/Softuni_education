import {html} from '../lib.js';
import {getItems} from '../api/data.js';
import {itemTemplate} from './common/item.js';


let allItemsTemplate = (data) => html`
    <section id="car-listings">
        <h1>Car Listings</h1>
        <div class="listings">
            ${data.length > 0 ? data.map(item => itemTemplate(item)) : html`<p class="no-cars">No cars in
                database.</p>`}
        </div>
    </section>`;

export async function allItems(context) {

    let data = await getItems();
    context.render(allItemsTemplate(data));
}