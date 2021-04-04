import {html} from '../../lib.js'
export let itemTemplate = (item) => html`
    <a class="article-preview" href="/details/${item._id}">
        <article>
            <h3>Topic: <span>${item.title}</span></h3>
            <p>Category: <span>${item.category}</span></p>
        </article>
    </a>`;