import {html} from '../lib.js';
import {getsearchItems} from '../api/data.js';
import {itemTemplate} from './common/item.js';



let searchTemplate = (onSubmit,data) => html`
    <section id="search-cars">
        <h1>Filter by year</h1>

        <div class="container">
            <input id="search-input" type="text" name="search" placeholder="Enter desired production year">
            <button @click=${onSubmit}class="button-list">Search</button>
        </div>

        <h2>Results:</h2>
        <div class="listings">
            ${data!==undefined?(data.length > 0 ? data.map(item => itemTemplate(item)) : html`<p class="no-cars"> No results.</p>`):html``}
        </div>
    </section>`;

export async function searchItems(context) {

    async function onSubmit(event){
        let year = event.target.parentElement.children[0]
        let data = await getsearchItems(Number(year.value));

        context.render(searchTemplate(onSubmit,data));
    }
    context.render(searchTemplate(onSubmit));
}