import {html} from '../lib.js';
import {getItemId} from '../api/data.js';

let detailsTemplate = (item, isOwner,onDelete) => html`
    <section id="meme-details">
        <h1>Meme Title: ${item.title}</h1>
        <div class="meme-details">
            <div class="meme-img">
                <img alt="meme-alt" src="${item.imageUrl}">
            </div>
            <div class="meme-description">
                <h2>Meme Description</h2>
                <p>
                    ${item.description}
                </p>

                <!-- Buttons Edit/Delete should be displayed only for creator of this meme  -->
                ${isOwner?html`<a class="button warning" href="/edit/${item._id}">Edit</a>
                <button @click = ${onDelete} class="button danger" >Delete</button>`:''}
            </div>
        </div>
    </section>
`;


export async function detailsPage(context) {
    let id = context.params.id;
    let userId = sessionStorage.getItem('userId');
    let item = await getItemId(id);
    context.render(detailsTemplate(item, item._ownerId == userId, onDelete));

    function onDelete(){
        context.page.redirect('/delete/' + context.params.id)
    }
}


