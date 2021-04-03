import {html} from '../lib.js'
import {getItems} from '../api/data.js';
import {itemTemplate} from './common/item.js';



let allItemsTemplate = (data) => html`
    <div id="dashboard-holder">
        ${data.length>0?data.map(item => itemTemplate(item))
        :html`<h1>No ideas yet! Be the first one :)</h1>`}
    </div>`;

export async function allItems(context) {
    let data = await getItems()
    context.render(allItemsTemplate(data))
}