import {logout} from '../api/data.js';

export async function logoutPage(context) {
    await logout();
    context.setUserNav();
    context.page.redirect('/');
}