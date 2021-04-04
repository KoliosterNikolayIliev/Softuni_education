import {html} from '../lib.js'
import {register} from '../api/data.js';


let registerTemplate = (onSubmit) => html`
    <section id="register-page" class="content auth">
        <h1>Register</h1>

        <form @submit=${onSubmit} id="register" action="#" method="">
            <fieldset>
                <blockquote>Knowledge is not simply another commodity. On the contrary. Knowledge is never used up.
                    It
                    increases by diffusion and grows by dispersion.</blockquote>
                <p class="field email">
                    <label for="register-email">Email:</label>
                    <input type="email" id="register-email" name="email" placeholder="maria@email.com">
                </p>
                <p class="field password">
                    <label for="register-pass">Password:</label>
                    <input type="password" name="password" id="register-pass">
                </p>
                <p class="field password">
                    <label for="register-rep-pass">Repeat password:</label>
                    <input type="password" name="rep-pass" id="register-rep-pass">
                </p>
                <p class="field submit">
                    <input class="btn submit" type="submit" value="Register">
                </p>
                <p class="field">
                    <span>If you already have profile click <a href="#">here</a></span>
                </p>
            </fieldset>
        </form>
    </section>`;


export async function registerPage(context) {
    console.log('register');
    context.render(registerTemplate(onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        let formData = new FormData(event.target);
        let email = formData.get('email').trim();
        let password = formData.get('password');
        let repass = formData.get('rep-pass');
        if (email == '' || password == '' || repass == '') {
            return alert('All fields must be filled!');
        } else if (password !== repass) {
            return alert('Passwords don\'t match!');
        }

        await register(email, password);
        event.target.reset()
        context.setUserNav();
        await context.page.redirect('/');
    }
}