import {logout} from '../api/data.js';

export async function logoutPage(context) {
    logout();
    context.setUserNav();
    context.page.redirect('/');
}