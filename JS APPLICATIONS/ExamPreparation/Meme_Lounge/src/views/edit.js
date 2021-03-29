import {html} from '../lib.js'
import {editRecord, getItemId} from '../api/data.js';

let editTemplate = (item, onSubmit) => html`
    <section id="edit-meme">
        <form @submit="${onSubmit} id="edit-form">
            <h1>Edit Meme</h1>
            <div class="container">
                <label for="title">Title</label>
                <input id="title" type="text" placeholder="Enter Title" name="title" .value="${item.title}">
                <label for="description">Description</label>
                <textarea id="description" placeholder="Enter Description" name="description">
                            ${item.description}
                        </textarea>
                <label for="imageUrl">Image Url</label>
                <input id="imageUrl" type="text" placeholder="Enter Meme ImageUrl" name="imageUrl" .value="${item.imageUrl}">
                <input type="submit" class="registerbtn button" value="Edit Meme">
            </div>
        </form>
    </section>`;


export async function editPage(context) {
    let id = context.params.id;
    let item = await getItemId(id);
    context.render(editTemplate(item, onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        let formData = new FormData(event.target);
        let data = {
            title: formData.get('title'),
            description: formData.get('description'),
            imageUrl: formData.get('imageUrl'),
        };
        if(data.title == ''|| data.description==''|| data.imageUrl==''){
            return alert('All fields are required!')
        }
        await editRecord(id, data);
        context.page.redirect('/');
    }
}