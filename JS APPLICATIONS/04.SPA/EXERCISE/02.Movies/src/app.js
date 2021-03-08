//import modules
//grab sections
//setup modules
//setup navigation

import {setupHome, showHome} from './home.js';
import {setupDetails} from './details.js';
import {setupLogin, showLogin} from './login.js';
import {setupRegister, showRegister} from './register.js';
import {setupCreate, showCreate} from './create.js';
import {setupEdit} from './edit.js';

let main = document.getElementsByTagName('main')[0];

let links = {
    'homeLink': showHome,
    'loginLink': showLogin,
    'registerLink': showRegister,
    'createLink': showCreate,

};

setupSection('home-page', setupHome);
setupSection('add-movie', setupCreate);
setupSection('movie-details', setupDetails);
setupSection('edit-movie', setupEdit);
setupSection('form-login', setupLogin);
setupSection('form-sign-up', setupRegister);

setupNavigation();

// Start application in home view
showHome();


function setupSection(sectionId, setup) {
    let section = document.getElementById(sectionId);
    setup(main, section);
}

function setupNavigation() {
    document.querySelector('nav').addEventListener('click', (event) => {
        let view = links[event.target.id];
        if (typeof view === 'function') {
            event.preventDefault();
            view();
        }

    });
    document.getElementById('createLink').addEventListener('click', (event) => {
        event.preventDefault();
        showCreate();
    });
}