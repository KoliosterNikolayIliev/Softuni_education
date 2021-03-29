import {html} from '../lib.js'

import {getUserItems} from '../api/data.js';


let myTemplate = (data,username,email,gender) => html`
    <section id="user-profile-page" class="user-profile">
        <article class="user-info">
            <img id="user-avatar-url" alt="user-profile" src="/images/${gender}.png">
            <div class="user-content">
                <p>Username: ${username}</p>
                <p>Email: ${email}</p>
                <p>My memes count: ${data.length}</p>
            </div>
        </article>
        <h1 id="user-listings-title">User Memes</h1>
        <div class="user-meme-listings">
            
            ${data.length>0 ? data.map(itemTemplateUser) : html`<p class="no-memes">No memes in database.</p>`}
            
        </div>
    </section>`;



export async function userItemsPage(context) {
    let username = sessionStorage.getItem('username')
    let email = sessionStorage.getItem('email')
    let gender = sessionStorage.getItem('gender')
    let data = await getUserItems()
    context.render(myTemplate(data,username,email,gender))
}

export let itemTemplateUser = (item) => html`
    <div class="user-meme">
        <p class="user-meme-title">${item.title}</p>
        <img class="userProfileImage" alt="meme-img" src="${item.imageUrl}">
        <a class="button" href="/details/${item._id}">Details</a>
    </div>`;