import {html} from '../lib.js'

import {getUserItems} from '../api/data.js';
import {itemTemplate} from './common/item.js';

let myTemplate = (data) => html`
    <div class="row space-top">
        <div class="col-md-12">
            <h1>My Furniture</h1>
            <p>This is a list of your publications.</p>
        </div>
    </div>
    <div class="row space-top">
        ${data.map(item=>itemTemplate(item))} 
<!-- {data.map(itemTemplate)} -->
    </div>`;



export async function userItemsPage(context) {
    let data = await getUserItems()
    context.render(myTemplate(data))
}