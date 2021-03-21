// import {html} from '../../node_modules/lit-html/lit-html.js'
import {html} from 'https://unpkg.com/lit-html?module';
import {getOwnFurniture} from '../api/data.js';
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



export async function ownFurniturePage(context) {
    let data = await getOwnFurniture()
    context.render(myTemplate(data))
}