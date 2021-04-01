import {html} from '../lib.js'
import {register} from '../api/data.js';


let registerTemplate = (onSubmit) => html`
    <section id="form-sign-up">
        <form @submit="${onSubmit}" class="text-center border border-light p-5" action="#" method="post">
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" placeholder="Email" name="email" value="">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" placeholder="Password" name="password" value="">
            </div>

            <div class="form-group">
                <label for="repeatPassword">Repeat Password</label>
                <input type="password" class="form-control" placeholder="Repeat-Password" name="repeatPassword" value="">
            </div>

            <button type="submit" class="btn btn-primary">Register</button>
        </form>
    </section>`;


export async function registerPage(context) {
    context.render(registerTemplate(onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        let formData = new FormData(event.target);
        let email = formData.get('email').trim();
        let password = formData.get('password');
        let repass = formData.get('repeatPassword');
        if (email == '' || password == '' || repass == '') {
            return alert('All fields must be filled!');
        } else if (password !== repass) {
            return alert('Passwords don\'t match!');
        } else if(password.length<6){
            return alert('The password should be at least 6 characters long!')
        }

        await register(email, password);

        context.setUserNav();
        await context.page.redirect('/');
    }
}