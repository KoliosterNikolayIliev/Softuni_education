import {html} from '../lib.js';
import {addLike, getItemId, getLikes, getUserLike, unLike} from '../api/data.js';

let detailsTemplate = (item, isOwner, likeUnlike, likesCount) => html`
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
                    ${isOwner ? html`
                        <div id="userBtns" style="display: inline">
                            <a class="btn btn-danger" href="/delete/${item._id}">Delete</a>
                            <a class="btn btn-warning" href="/edit/${item._id}">Edit</a>
                        </div>` : ''}
                    ${!isOwner ? html`<a @click=${likeUnlike} class="btn btn-primary"
                                         href="javascript:void(0)">Like</a>` : ''}

                    <span id="likesCounter" class="enrolled-span">Likes ${likesCount}</span>
                </div>
            </div>
        </div>
    </section>`;

export async function detailsPage(context) {
    let id = context.params.id;
    let userId = sessionStorage.getItem('userId');
    let item = await getItemId(id);
    async function likeUnlike() {
        if (!userId) {
            return context.page.redirect('/login');
        }
        let likeList = await getUserLike(id);
        let like = likeList[0]
        if (likeList.length > 0) {
            await unLike(like._id);
            context.render(detailsTemplate(item, item._ownerId == userId, likeUnlike, await getLikes(id)));
        } else {
            await addLike({movieId: item._id});
            context.render(detailsTemplate(item, item._ownerId == userId, likeUnlike, await getLikes(id)));
        }
    }

    context.render(detailsTemplate(item, item._ownerId == userId, likeUnlike, await getLikes(id)));

}


