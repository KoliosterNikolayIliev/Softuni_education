import {html} from '../lib.js';
import {createRecord} from '../api/data.js';


let createTemplate = (onSubmit) => html`
    <section id="create-listing">
        <div class="container">
            <form @submit="${onSubmit}" id="create-form">
                <h1>Create Car Listing</h1>
                <p>Please fill in this form to create an listing.</p>
                <hr>

                <p>Car Brand</p>
                <input type="text" placeholder="Enter Car Brand" name="brand">

                <p>Car Model</p>
                <input type="text" placeholder="Enter Car Model" name="model">

                <p>Description</p>
                <input type="text" placeholder="Enter Description" name="description">

                <p>Car Year</p>
                <input type="number" placeholder="Enter Car Year" name="year">

                <p>Car Image</p>
                <input type="text" placeholder="Enter Car Image" name="imageUrl">

                <p>Car Price</p>
                <input type="number" placeholder="Enter Car Price" name="price">

                <hr>
                <input type="submit" class="registerbtn" value="Create Listing">
            </form>
        </div>
    </section>`;


export async function createPage(context) {

    context.render(createTemplate(onSubmit));

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

        await createRecord(data);
        context.page.redirect('/allItems');
    }
}
