import {html} from '../../node_modules/lit-html/lit-html.js';
import {editRecord, getItemId} from '../api/data.js';

let editTemplate = (item, onSubmit) => html`
    <form @submit=${onSubmit}>
        <div class="row space-top">
            <div class="col-md-4">
                <div class="form-group">
                    <label class="form-control-label" for="new-make">Make</label>
                    <input class="form-control" id="new-make" type="text" name="make" .value${item.make}>
                </div>
                <div class="form-group has-success">
                    <label class="form-control-label" for="new-model">Model</label>
                    <input class="form-control is-valid" id="new-model" type="text" name="model" value="Swedish">
                </div>
                <div class="form-group has-danger">
                    <label class="form-control-label" for="new-year">Year</label>
                    <input class="form-control is-invalid" id="new-year" type="number" name="year" value="2015">
                </div>
                <div class="form-group">
                    <label class="form-control-label" for="new-description">Description</label>
                    <input class="form-control" id="new-description" type="text" name="description"
                           value="Medium table">
                </div>
            </div>
            <div class="col-md-4">
                <div class="form-group">
                    <label class="form-control-label" for="new-price">Price</label>
                    <input class="form-control" id="new-price" type="number" name="price" value="235">
                </div>
                <div class="form-group">
                    <label class="form-control-label" for="new-image">Image</label>
                    <input class="form-control" id="new-image" type="text" name="img" value="/images/table.png">
                </div>
                <div class="form-group">
                    <label class="form-control-label" for="new-material">Material (optional)</label>
                    <input class="form-control" id="new-material" type="text" name="material" value="Wood">
                </div>
                <input type="submit" class="btn btn-info" value="Edit"/>
            </div>
        </div>
    </form>`;


export async function editPage(context) {
    let id = context.params.id;
    let item = getItemId(id);
    context.render(editTemplate(item, onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        let formData = new FormData(event.target);
        let itemData = {};
        for (const item of Array.from(formData.entries())) {
            itemData[item[0]] = item[1];
        }
        if (Object.entries(itemData).filter(([k, v]) => k !== 'material').some(([k, v]) => v === '')) {
            return alert('Please fill all mandatory fields!');
        }
        itemData.year = Number(itemData.year)
        itemData.price = Number(itemData.price)
        await editRecord(id,itemData)
        context.page.redirect('/')
    }
}