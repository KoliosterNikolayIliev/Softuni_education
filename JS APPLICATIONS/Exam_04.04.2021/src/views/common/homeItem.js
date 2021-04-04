import {html} from '../../lib.js'
export let homeItemTemplate = (item) => html`
    <article>
        <h3>${item.title}</h3>
        <p>${item.content}</p>
        <a href="/details/${item._id}" class="btn details-btn">Details</a>
    </article>`;