import {html} from '../lib.js'
import {register} from '../api/data.js';


let registerTemplate = (onSubmit) => html`
    <section id="register">
        <form @submit="${onSubmit} id="register-form">
            <div class="container">
                <h1>Register</h1>
                <label for="username">Username</label>
                <input id="username" type="text" placeholder="Enter Username" name="username">
                <label for="email">Email</label>
                <input id="email" type="text" placeholder="Enter Email" name="email">
                <label for="password">Password</label>
                <input id="password" type="password" placeholder="Enter Password" name="password">
                <label for="repeatPass">Repeat Password</label>
                <input id="repeatPass" type="password" placeholder="Repeat Password" name="repeatPass">
                <div class="gender">
                    <input type="radio" name="gender" id="female" value="female">
                    <label for="female">Female</label>
                    <input type="radio" name="gender" id="male" value="male" checked>
                    <label for="male">Male</label>
                </div>
                <input type="submit" class="registerbtn button" value="Register">
                <div class="container signin">
                    <p>Already have an account?<a href="#">Sign in</a>.</p>
                </div>
            </div>
        </form>
    </section>`;


export async function registerPage(context) {
    context.render(registerTemplate(onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        let formData = new FormData(event.target);
        let email = formData.get('email').trim();
        let password = formData.get('password');
        let repass = formData.get('repeatPass');
        let gender = formData.get('gender');
        let username = formData.get('username')

        if (email == '' || password == '' || repass == '' || gender == '' || username == '') {
            return alert('All fields must be filled!');
        } else if (password !== repass) {

            return alert('Passwords don\'t match!');
        }

        await register(email, password,username, gender);

        context.setUserNav();
        await context.page.redirect('/');
    }
}