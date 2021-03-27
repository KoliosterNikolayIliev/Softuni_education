import {html} from '../lib.js'
import {getItems} from '../api/data.js';
import {itemTemplate} from './common/item.js';

let dashboardTemplate = (data) => html`
    <div class="row space-top">
        <div class="col-md-12">
            <h1>Welcome to Furniture System</h1>
            <p>Select furniture from the catalog to view details.</p>
        </div>
    </div>
    <div class="row space-top">
        ${data.map(item=>itemTemplate(item))} 
<!-- {data.map(itemTemplate)} -->
    </div>`;



export async function indexPage(context) {
    let data = await getItems()
    context.render(dashboardTemplate(data))
}