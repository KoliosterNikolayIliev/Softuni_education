import {html} from '../lib.js'

import {getUserItems} from '../api/data.js';
import {itemTemplate} from './common/item.js';

let myTemplate = (data) => html`
    `;



export async function userItemsPage(context) {
    console.log('userItems');
    // let data = await getUserItems()
    // context.render(myTemplate(data))
}