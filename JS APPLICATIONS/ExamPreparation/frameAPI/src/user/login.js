import {html} from '../lib.js'

import {login} from '../api/data.js';


let loginTemplate = (onSubmit) => html`
    `;


export async function loginPage(context) {
    console.log('login');
    // context.render(loginTemplate(onSubmit));
    //
    // async function onSubmit(event) {
    //     event.preventDefault();
    //     let formData = new FormData(event.target);
    //     let email = formData.get('email').trim();
    //     let password = formData.get('password');
    //     await login(email, password);
    //
    //     context.setUserNav();
    //     await context.page.redirect('/');
    // }
}

