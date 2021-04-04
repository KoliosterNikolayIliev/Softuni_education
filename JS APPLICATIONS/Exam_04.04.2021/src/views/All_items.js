import {html} from '../lib.js'
import {getItems} from '../api/data.js';
import {itemTemplate} from './common/item.js';



let allItemsTemplate = (data) => html`
`;

export async function allItems(context) {
    console.log('allitems');
    // let data = await getItems()
    // context.render(allItems(data))
}