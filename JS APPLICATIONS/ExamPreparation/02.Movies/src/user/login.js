import {html} from '../lib.js'

import {login} from '../api/data.js';


let loginTemplate = (onSubmit) => html`
    <section @submit="${onSubmit} id="form-login">
        <form class="text-center border border-light p-5" action="" method="">
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" placeholder="Email" name="email" value="">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" placeholder="Password" name="password" value="">
            </div>

            <button type="submit" class="btn btn-primary">Login</button>
        </form>
    </section>`;


export async function loginPage(context) {
    context.render(loginTemplate(onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        let formData = new FormData(event.target);
        let email = formData.get('email').trim();
        let password = formData.get('password').trim();
        await login(email, password);

        context.setUserNav();
        await context.page.redirect('/');
    }
}

