import {html} from '../lib.js';
import {createRecord} from '../api/data.js';

// let validData = {
//     make: false,
//     model: false,
//     year: false,
//     description: false,
//     price: false,
//     img: false,
// };

let createTemplate = (onSubmit, validData) => html`
    `;


export async function createPage(context) {
    console.log('create');
    // validData = {
    //     make: false,
    //     model: false,
    //     year: false,
    //     description: false,
    //     price: false,
    //     img: false,
    // };
    // context.render(createTemplate(onSubmit, validData));
    //
    // async function onSubmit(event) {
    //     event.preventDefault();
    //     let formData = new FormData(event.target);
    //     let data = {
    //         make: formData.get('make'),
    //         model: formData.get('model'),
    //         year: Number(formData.get('year')),
    //         description: formData.get('description'),
    //         price: Number(formData.get('price')),
    //         img: formData.get('img'),
    //         material: formData.get('material'),
    //     };
    //     if (data.make.length < 4) {
    //         validData.make = false;
    //         context.render(createTemplate(onSubmit, validData));
    //         return alert('Make must be at least 4 symbols long!');
    //     }else{validData.make = true;}
    //     if (data.model.length < 4) {
    //         validData.model = false;
    //         context.render(createTemplate(onSubmit, validData));
    //         return alert('Model must be at least 4 symbols long!');
    //     }else{validData.model = true;}
    //     if (data.year < 1950 || data.year > 2050) {
    //         validData.year = false;
    //         context.render(createTemplate(onSubmit, validData));
    //         return alert('Year must be between 1950 and 2050!');
    //     }else{validData.year = true;}
    //     if (data.description.length < 10) {
    //         validData.description = false;
    //         context.render(createTemplate(onSubmit, validData));
    //         return alert('Description must be at least 10 symbols long!');
    //     }else{validData.description = true;}
    //     if (data.price <= 0) {
    //         validData.price = false;
    //         context.render(createTemplate(onSubmit, validData));
    //         return alert('Price must be above 0!');
    //     }else{validData.price = true;}
    //     if (data.img === '') {
    //         validData.img = false;
    //         context.render(createTemplate(onSubmit, validData));
    //         return alert('Image URL is required!');
    //     }else{validData.img = true;}
    //
    //     await createRecord(data);
    //     context.page.redirect('/');
    // }
}
