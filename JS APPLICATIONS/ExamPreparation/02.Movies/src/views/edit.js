import {html} from '../lib.js'
import {editRecord, getItemId} from '../api/data.js';


let editTemplate = (item, onSubmit) => html`
    <section  id="edit-movie">
        <form @submit="${onSubmit}" class="text-center border border-light p-5" action="#" method="">
            <h1>Edit Movie</h1>
            <div class="form-group">
                <label for="title">Movie Title</label>
                <input id="title" type="text" class="form-control" placeholder="Movie Title" .value="${item.title}" name="title">
            </div>
            <div class="form-group">
                <label for="description">Movie Description</label>
                <textarea id="description" class="form-control" placeholder="Movie Description..." name="description">${item.description}</textarea>
            </div>
            <div class="form-group">
                <label for="imageUrl">Image url</label>
                <input id="imageUrl" type="text" class="form-control" placeholder="Image Url" value="${item.img}" name="imageUrl">
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </section>`;


export async function editPage(context) {
    let id = context.params.id;
    let item = await getItemId(id);
    let owner = sessionStorage.getItem('userId');
    context.render(editTemplate(item, onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        let formData = new FormData(event.target);
        let data = {
            title: formData.get('title'),
            description: formData.get('description'),
            img: formData.get('imageUrl'),
            _ownerId: owner,
        };

        if (data.title == '' || data.img == '' || data.description == '') {
            return alert('All fields must be filled!');
        }
        await editRecord(id, data);
        context.page.redirect('/details/'+ id);
    }
}