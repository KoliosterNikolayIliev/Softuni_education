import {html} from '../lib.js'

import {login} from '../api/data.js';


let loginTemplate = (onSubmit) => html`
    <section id="login-page" class="content auth">
        <h1>Login</h1>

        <form @submit = ${onSubmit} id="login" action="#" method="">
            <fieldset>
                <blockquote>Knowledge is like money: to be of value it must circulate, and in circulating it can
                    increase in quantity and, hopefully, in value</blockquote>
                <p class="field email">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" placeholder="maria@email.com">
                </p>
                <p class="field password">
                    <label for="login-pass">Password:</label>
                    <input type="password" id="login-pass" name="password">
                </p>
                <p class="field submit">
                    <input class="btn submit" type="submit" value="Log in">
                </p>
                <p class="field">
                    <span>If you don't have profile click <a href="/register">here</a></span>
                </p>
            </fieldset>
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
        event.target.reset()

        context.setUserNav();
        await context.page.redirect('/');
    }
}

