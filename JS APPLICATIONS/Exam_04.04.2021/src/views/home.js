import {html} from '../lib.js'
import {getItems} from '../api/data.js';
import {itemTemplate} from './common/item.js';

let homeTemplate = (data) => html`
    `;



export async function indexPage(context) {
    console.log('index')
    // let data = await getItems()
    // context.render(homeTemplate(data))
}