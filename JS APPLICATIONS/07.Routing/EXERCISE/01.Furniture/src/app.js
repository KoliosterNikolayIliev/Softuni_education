import page from '../node_modules/page/page.mjs'
import {render} from '../../node_modules/lit-html/lit-html.js'

let main = document.getElementsByClassName('container')[0];

import {createPage} from './views/create.js';
import {dashboardPage} from './views/dashboard.js';
import {editPage} from './views/edit.js';
import {registerPage} from './user/register.js';
import {loginPage} from './user/login.js';
import {ownFurniturePage} from './views/my-furniture.js';
import {detailsPage} from './views/details.js';
import {logoutPage} from './user/logout.js';



page('/', decorateContext, dashboardPage);
page('/my-furniture', decorateContext, ownFurniturePage);
page('/details/:id', decorateContext, detailsPage);
page('/create', decorateContext, createPage);
page('/edit/:id', decorateContext, editPage);
page('/register', decorateContext, registerPage);
page('/login', decorateContext, loginPage);
page('/logout', decorateContext, logoutPage);

setUserNav()
page.start();


function decorateContext(context, next) {
    context.render = (content) => render(content, main);
    context.setUserNav = setUserNav
    next();
}

function setUserNav(){
    let userId = sessionStorage.getItem('userId')
    if (userId!==null){
        document.getElementById('user').style.display = 'inline-block'
        document.getElementById('guest').style.display = 'none'
    }else {
        document.getElementById('user').style.display = 'none'
        document.getElementById('guest').style.display = 'inline-block'
    }
}




