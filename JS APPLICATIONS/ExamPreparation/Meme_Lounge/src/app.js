import page from './lib.js'
import {render} from './lib.js'

// the holder for our future views
let main = document.getElementsByTagName('main')[0];


import {createPage} from './views/create.js';
import {indexPage} from './views/home.js';
import {editPage} from './views/edit.js';
import {registerPage} from './user/register.js';
import {loginPage} from './user/login.js';
import {userItemsPage} from './views/userItemDetails.js';
import {detailsPage} from './views/details.js';
import {logoutPage} from './user/logout.js';
import {deletePage} from './views/delete.js';
import {allMemes} from './views/allmemes.js';



page('/', decorateContext, indexPage);
page('/allmemes', decorateContext, allMemes);
page('/userItems', decorateContext, userItemsPage);
page('/details/:id', decorateContext, detailsPage);
page('/create', decorateContext, createPage);
page('/edit/:id', decorateContext, editPage);
page('/register', decorateContext, registerPage);
page('/login', decorateContext, loginPage);
page('/logout', decorateContext, logoutPage);
page('/delete/:id', decorateContext, deletePage);

setUserNav()
page.start();

//here other useful stuff can be loaded
function decorateContext(context, next) {
    context.render = (content) => render(content, main);
    context.setUserNav = setUserNav
    next();
}

function setUserNav(){

    let userId = sessionStorage.getItem('userId')
    if (userId!==null){
        let email = sessionStorage.getItem('email')
        document.getElementsByClassName('user')[0].style.display = 'inline-block'
        document.getElementsByClassName('guest')[0].style.display = 'none'
        document.getElementById('userMail').innerHTML = `Welcome, ${email}`
    }else {
        document.getElementsByClassName('user')[0].style.display = 'none'
        document.getElementsByClassName('guest')[0].style.display = 'inline-block'
    }
}




