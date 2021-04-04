import {html} from '../lib.js'
import {getItems} from '../api/data.js';
import {itemTemplate} from './common/item.js';



let allItemsTemplate = (data) => html`
    <section id="catalog-page" class="content catalogue">
        <h1>All Articles</h1>
        ${data.length > 0 ? data.map(item => itemTemplate(item)): html`<h3 class="no-articles">No articles yet</h3>`}
    </section>`;

export async function allItems(context) {
    let data = await getItems()
    context.render(allItemsTemplate(data))
}