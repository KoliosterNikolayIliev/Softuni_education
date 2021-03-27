import {html} from '../lib.js'
import {editRecord, getItemId} from '../api/data.js';

let validData = {
    make: true,
    model: true,
    year: true,
    description: true,
    price: true,
    img: true,
};

let editTemplate = (item, onSubmit, validData) => html`
    <div class="row space-top">
        <div class="col-md-12">
            <h1>Edit Furniture</h1>
            <p>Please fill all fields.</p>
        </div>
    </div>
    <form @submit=${onSubmit}>
        <div class="row space-top">
            <div class="col-md-4">
                <div class="form-group">
                    <label class="form-control-label" for="new-make">Make</label>
                    <input class=${'form-control' + ' '+ (validData.make ? 'is-valid' : 'is-invalid')} id="new-make"
                           type="text" name="make" .value=${item.make}>
                </div>
                <div class="form-group has-success">
                    <label class="form-control-label" for="new-model">Model</label>
                    <input class=${'form-control' +  ' '+ (validData.model ? 'is-valid' : 'is-invalid')} id="new-model"
                           type="text" name="model" .value=${item.model}>
                </div>
                <div class="form-group has-danger">
                    <label class="form-control-label" for="new-year">Year</label>
                    <input class=${'form-control' +  ' '+ (validData.year ? 'is-valid' : 'is-invalid')} id="new-year"
                           type="number" name="year" .value=${item.year}>
                </div>
                <div class="form-group">
                    <label class="form-control-label" for="new-description">Description</label>
                    <input class=${'form-control' +  ' '+ (validData.description ? 'is-valid' : 'is-invalid')}
                           id="new-description" type="text" name="description"
                           .value=${item.description}>
                </div>
            </div>
            <div class="col-md-4">
                <div class="form-group">
                    <label class="form-control-label" for="new-price">Price</label>
                    <input class=${'form-control' +  ' '+ (validData.price ? 'is-valid' : 'is-invalid')} id="new-price"
                           type="number" name="price" .value=${item.price}>
                </div>
                <div class="form-group">
                    <label class="form-control-label" for="new-image">Image</label>
                    <input class=${'form-control' +  ' '+ (validData.img ? 'is-valid' : 'is-invalid')} id="new-image"
                           type="text" name="img" .value=${item.img}>
                </div>
                <div class="form-group">
                    <label class="form-control-label" for="new-material">Material (optional)</label>
                    <input class="form-control" id="new-material" type="text" name="material" .value=${item.material}>
                </div>
                <input type="submit" class="btn btn-info" value="Edit"/>
            </div>
        </div>
    </form>`;


export async function editPage(context) {
    let id = context.params.id;
    let item = await getItemId(id);

    context.render(editTemplate(item, onSubmit,validData));

    async function onSubmit(event) {
        event.preventDefault();
        let formData = new FormData(event.target);
        let data = {
            make: formData.get('make'),
            model: formData.get('model'),
            year: Number(formData.get('year')),
            description: formData.get('description'),
            price: Number(formData.get('price')),
            img: formData.get('img'),
            material: formData.get('material'),
        };

        if (data.make.length < 4) {
            validData.make = false;
            context.render(editTemplate(item, onSubmit, validData));
            return alert('Make must be at least 4 symbols long!');
        }else{validData.make = true;}
        if (data.model.length < 4) {
            validData.model = false;
            context.render(editTemplate(item, onSubmit, validData));
            return alert('Model must be at least 4 symbols long!');
        }else{validData.model = true;}
        if (data.year < 1950 || data.year > 2050) {
            validData.year = false;
            context.render(editTemplate(item, onSubmit, validData));
            return alert('Year must be between 1950 and 2050!');
        }else{validData.year = true;}
        if (data.description.length < 10) {
            validData.description = false;
            context.render(editTemplate(item, onSubmit, validData));
            return alert('Description must be at least 10 symbols long!');
        }else{validData.description = true;}
        if (data.price <= 0) {
            validData.price = false;
            context.render(editTemplate(item, onSubmit, validData));
            return alert('Price must be above 0!');
        }else{validData.price = true;}
        if (data.img === '') {
            validData.img = false;
            context.render(editTemplate(item, onSubmit, validData));
            return alert('Image URL is required!');
        }else{validData.img = true;}
        await editRecord(id, data);
        context.page.redirect('/');
    }
}