import {html} from '../lib.js'
import {register} from '../api/data.js';


let registerTemplate = (onSubmit) => html`
    `;


export async function registerPage(context) {
    console.log('register');
    // context.render(registerTemplate(onSubmit));
    //
    // async function onSubmit(event) {
    //     event.preventDefault();
    //     let formData = new FormData(event.target);
    //     let email = formData.get('email').trim();
    //     let password = formData.get('password');
    //     let repass = formData.get('rePass');
    //     if (email == '' || password == '' || repass == '') {
    //         return alert('All fields must be filled!');
    //     } else if (password !== repass) {
    //         return alert('Passwords don\'t match!');
    //     }
    //
    //     await register(email, password);
    //
    //     context.setUserNav();
    //     await context.page.redirect('/');
    // }
}