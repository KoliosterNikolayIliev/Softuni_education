import {html} from '../lib.js'
import {getItems} from '../api/data.js';
import {itemTemplate} from './common/item.js';



let allMemesTemplate = (data) => html`
    <section id="meme-feed">
        <h1>All Memes</h1>
        <div id="memes">
            ${data.length>0 ? data.map(item=>itemTemplate(item)) : html`<p class="no-memes">No memes in database.</p>`}
        </div>
    </section>`;

export async function allMemes(context) {

    let data = await getItems()
    context.render(allMemesTemplate(data))
}


