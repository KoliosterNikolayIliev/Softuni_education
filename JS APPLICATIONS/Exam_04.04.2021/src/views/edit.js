import {html} from '../lib.js'
import {editRecord, getItemId} from '../api/data.js';


let editTemplate = (item, onSubmit) => html`
    <section id="edit-page" class="content">
        <h1>Edit Article</h1>

        <form @submit=${onSubmit} id="edit" action="#" method="">
            <fieldset>
                <p class="field title">
                    <label for="title">Title:</label>
                    <input type="text" name="title" id="title" placeholder="Enter article title" .value = ${item.title}>
                </p>

                <p class="field category">
                    <label for="category">Category:</label>
                    <input type="text" name="category" id="category" placeholder="Enter article category" .value = ${item.category}>
                </p>
                <p class="field">
                    <label for="content">Content:</label>
                    <textarea name="content" id="content">${item.content}</textarea>
                </p>

                <p class="field submit">
                    <input class="btn submit" type="submit" value="Save Changes">
                </p>

            </fieldset>
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
            category: formData.get('category'),
            content: formData.get('content'),
        };
        for (const field of Object.values(data)) {
            if (field == '') {
                return alert('All fields are required!');
            }
        }
        if (data.category == 'JavaScript' || data.category == 'C#' || data.category == 'Java' || data.category == 'Python') {
        }else {return alert('The category must be one of "JavaScript", "C#", "Java", or "Python".');}


        await editRecord(id, data);
        context.page.redirect('/details'+ id);
    }
}