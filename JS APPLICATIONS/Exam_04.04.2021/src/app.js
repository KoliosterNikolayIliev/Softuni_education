import page from './lib.js'
import {render} from './lib.js'

// the holder for our future views
let main = document.getElementById('main-content');


import {createPage} from './views/create.js';
import {indexPage} from './views/home.js';
import {editPage} from './views/edit.js';
import {registerPage} from './user/register.js';
import {loginPage} from './user/login.js';
import {userItemsPage} from './views/userItemDetails.js';
import {detailsPage} from './views/details.js';
import {logoutPage} from './user/logout.js';
import {deletePage} from './views/delete.js';
import {allItems} from './views/All_items.js';
import {searchItems} from './views/search.js';



page('/', decorateContext, indexPage);
page('/allItems', decorateContext, allItems);
page('/userItems', decorateContext, userItemsPage);
page('/details/:id', decorateContext, detailsPage);
page('/create', decorateContext, createPage);
page('/edit/:id', decorateContext, editPage);
page('/register', decorateContext, registerPage);
page('/login', decorateContext, loginPage);
page('/logout', decorateContext, logoutPage);
page('/delete/:id', decorateContext, deletePage);
page('/search', decorateContext, searchItems);

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
        document.getElementById('user').style.display = 'inline-block'
        document.getElementById('guest').style.display = 'none'
    }else {
        document.getElementById('user').style.display = 'none'
        document.getElementById('guest').style.display = 'inline-block'
    }
}

//<script src="./src/app.js" type="module" ></script>


