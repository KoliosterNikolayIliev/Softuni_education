import {html} from '../lib.js'
import {editRecord, getItemId} from '../api/data.js';



let editTemplate = (item, onSubmit) => html`
    <section id="edit-listing">
        <div class="container">

            <form @submit="${onSubmit}" id="edit-form">
                <h1>Edit Car Listing</h1>
                <p>Please fill in this form to edit an listing.</p>
                <hr>

                <p>Car Brand</p>
                <input type="text" placeholder="Enter Car Brand" name="brand" .value="${item.brand}">

                <p>Car Model</p>
                <input type="text" placeholder="Enter Car Model" name="model" .value="${item.model}">

                <p>Description</p>
                <input type="text" placeholder="Enter Description" name="description" .value="${item.description}">

                <p>Car Year</p>
                <input type="number" placeholder="Enter Car Year" name="year" .value="${Number(item.year)}">

                <p>Car Image</p>
                <input type="text" placeholder="Enter Car Image" name="imageUrl" .value="${item.imageUrl}">

                <p>Car Price</p>
                <input type="number" placeholder="Enter Car Price" name="price" .value="${Number(item.price)}">

                <hr>
                <input type="submit" class="registerbtn" value="Edit Listing">
            </form>
        </div>
    </section>`;


export async function editPage(context) {
    let id = context.params.id;
    let item = await getItemId(id);

    context.render(editTemplate(item, onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        let formData = new FormData(event.target);
        let data = {
            brand: formData.get('brand'),
            model: formData.get('model'),
            description: formData.get('description'),
            year: Number(formData.get('year')),
            imageUrl: formData.get('imageUrl'),
            price: Number(formData.get('price')),
        };
        for (const field of Object.values(data)) {
            if(field ==''){
                return alert('All fields are required!')
            }
        }
        if(data.price<0){return alert('Price must be positive number!')}
        if(data.year<0){return alert('Year must be positive number!')}
        await editRecord(id, data);
        context.page.redirect('/details/'+id);
    }
}