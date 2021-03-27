import {html} from '../lib.js'
import {register} from '../api/data.js';


let registerTemplate = (onSubmit) => html`
    <div class="row space-top">
        <div class="col-md-12">
            <h1>Register New User</h1>
            <p>Please fill all fields.</p>
        </div>
    </div>
    <form @submit="${onSubmit}">
        <div class="row space-top">
            <div class="col-md-4">
                <div class="form-group">
                    <label class="form-control-label" for="email">Email</label>
                    <input class="form-control" id="email" type="text" name="email">
                </div>
                <div class="form-group">
                    <label class="form-control-label" for="password">Password</label>
                    <input class="form-control" id="password" type="password" name="password">
                </div>
                <div class="form-group">
                    <label class="form-control-label" for="rePass">Repeat</label>
                    <input class="form-control" id="rePass" type="password" name="rePass">
                </div>
                <input type="submit" class="btn btn-primary" value="Register"/>
            </div>
        </div>
    </form>`;


export async function registerPage(context) {
    context.render(registerTemplate(onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        let formData = new FormData(event.target);
        let email = formData.get('email').trim();
        let password = formData.get('password');
        let repass = formData.get('rePass');
        if (email == '' || password == '' || repass == '') {
            return alert('All fields must be filled!');
        } else if (password !== repass) {
            return alert('Passwords don\'t match!');
        }

        await register(email, password);

        context.setUserNav();
        await context.page.redirect('/');
    }
}