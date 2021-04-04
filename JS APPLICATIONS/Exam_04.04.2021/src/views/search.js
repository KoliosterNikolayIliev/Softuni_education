import {html} from '../lib.js';
import {getsearchItems} from '../api/data.js';
import {itemTemplate} from './common/item.js';



let searchTemplate = (onSubmit,data) => html`
    <section id="search-page" class="content">
        <h1>Search</h1>
        <form @submit=${onSubmit} id="search-form">
            <p class="field search">
                <input id="searchField1" type="text" placeholder="Search by article title" name="search">
            </p>
            <p class="field submit">
                <input class="btn submit" type="submit" value="Search">
            </p>
        </form>
        <div class="search-container">
            ${data!==undefined?(data.length > 0 ? data.map(item => itemTemplate(item)) : html`<h3 class="no-articles">No matching articles</h3>`):html``}
            
        </div>
    </section>`;

export async function searchItems(context) {

    async function onSubmit(event){
        event.preventDefault()
        let title = document.getElementById('searchField1')
        let data = await getsearchItems(title.value);
        console.log(title);
        console.log(data);

        context.render(searchTemplate(onSubmit,data));
    }
    context.render(searchTemplate(onSubmit));
}