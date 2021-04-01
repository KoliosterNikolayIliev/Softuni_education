import {html} from '../lib.js'
import {register} from '../api/data.js';


let registerTemplate = (onSubmit) => html`
    <section id="register">
        <div class="container">
            <form @submit="${onSubmit} id="register-form">
                <h1>Register</h1>
                <p>Please fill in this form to create an account.</p>
                <hr>

                <p>Username</p>
                <input type="text" placeholder="Enter Username" name="username" required>

                <p>Password</p>
                <input type="password" placeholder="Enter Password" name="password" required>

                <p>Repeat Password</p>
                <input type="password" placeholder="Repeat Password" name="repeatPass" required>
                <hr>

                <input type="submit" class="registerbtn" value="Register">
            </form>
            <div class="signin">
                <p>Already have an account?
                    <a href="/login">Sign in</a>.
                </p>
            </div>
        </div>
    </section>`;


export async function registerPage(context) {
    console.log('register');
    context.render(registerTemplate(onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        let formData = new FormData(event.target);
        let username = formData.get('username').trim();
        let password = formData.get('password');
        let repass = formData.get('repeatPass');
        if (username == '' || password == '' || repass == '') {
            return alert('All fields must be filled!');
        } else if (password !== repass) {
            return alert('Passwords don\'t match!');
        }

        await register(username, password);

        context.setUserNav();
        await context.page.redirect('/allItems');
    }
}