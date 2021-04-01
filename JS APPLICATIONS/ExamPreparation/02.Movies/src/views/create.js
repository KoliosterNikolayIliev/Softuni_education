import {html} from '../lib.js';
import {createRecord} from '../api/data.js';


let createTemplate = (onSubmit) => html`
    <section id=" add-movie">
    <form @submit="${onSubmit}" class="text-center border border-light p-5" action="#" method="">
        <h1>Add Movie</h1>
        <div class="form-group">
            <label for="title">Movie Title</label>
            <input type="text" class="form-control" placeholder="Title" name="title" value="">
        </div>
        <div class="form-group">
            <label for="description">Movie Description</label>
            <textarea class="form-control" placeholder="Description" name="description"></textarea>
        </div>
        <div class="form-group">
            <label for="imageUrl">Image url</label>
            <input type="text" class="form-control" placeholder="Image Url" name="imageUrl" value="">
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    </section>`;


export async function createPage(context) {
    context.render(createTemplate(onSubmit));
    let owner = sessionStorage.getItem('userId');

    async function onSubmit(event) {
        event.preventDefault();
        let formData = new FormData(event.target);
        let data = {
            title: formData.get('title'),
            description: formData.get('description'),
            img: formData.get('imageUrl'),
            _ownerId: owner,
            //TODO
            // likes:[]
        };
        if (data.title == '' || data.img == '' || data.description == '') {
            return alert('All fields must be filled!');
        }
        await createRecord(data);
        context.page.redirect('/');
    }
}
