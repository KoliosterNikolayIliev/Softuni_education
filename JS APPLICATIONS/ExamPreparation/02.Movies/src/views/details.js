import {html} from '../lib.js';
import {getItemId} from '../api/data.js';

let detailsTemplate = (item, isOwner) => html`
    <section id="movie-example">
        <div class="container">
            <div class="row bg-light text-dark">
                <h1>Movie title: ${item.title}</h1>

                <div class="col-md-8">
                    <img class="img-thumbnail" src="${item.img}"
                         alt="Movie">
                </div>
                <div class="col-md-4 text-center">
                    <h3 class="my-3 ">Movie Description</h3>
                    <p>${item.description}</p>
                    ${isOwner?html`<div id="userBtns" style="display: inline">
                        <a class="btn btn-danger" href="/delete/${item._id}">Delete</a>
                        <a class="btn btn-warning" href="/edit/${item._id}">Edit</a>
                    </div>`:''}
                    ${!isOwner?html`<a class="btn btn-primary" href="/like">Like</a>`:''}
                    <span class="enrolled-span">Liked 1</span>
                </div>
            </div>
        </div>
    </section>`;


export async function detailsPage(context) {
    let id = context.params.id;
    let userId = sessionStorage.getItem('userId');
    let item = await getItemId(id);
    context.render(detailsTemplate(item, item._ownerId == userId));
}


