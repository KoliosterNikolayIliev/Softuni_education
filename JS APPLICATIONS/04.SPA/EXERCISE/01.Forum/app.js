let commentedTitle = `<div class="theme-title">
                        <div class="theme-name-wrapper">
                            <div class="theme-name">
                                <h2>Angular 10</h2>
                                <p>Date:
                                    <time>2020-10-10 12:08:28</time>
                                </p>
                            </div>
                            <div class="subscribers">
                                <p>Subscribers: <span>456</span></p>
                                <!-- <button class="subscribe">Subscribe</button>
                                <button class="unsubscribe">Unsubscribe</button> -->
                            </div>
                        </div>
                    </div>`;

let comment = `<div class="comment">
                        <header class="header">
                            <p><span>David</span> posted on
                                <time>2020-10-10 12:08:28</time>
                            </p>
                        </header>
                        <div class="comment-main">
                            <div class="userdetails">
                                <img src="./static/profile.png" alt="avatar">
                            </div>
                            <div class="post-content">
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure facere sint dolorem
                                    quam,
                                    accusantium ipsa veniam laudantium inventore aut, tenetur quibusdam doloribus.
                                    Incidunt odio
                                    nostrum facilis ipsum dolorem deserunt illum?</p>
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure facere sint dolorem
                                    quam,
                                    accusantium ipsa veniam laudantium inventore aut, tenetur quibusdam doloribus.
                                    Incidunt odio
                                    nostrum facilis ipsum dolorem deserunt illum?</p>
                            </div>
                        </div>
                        <div class="footer">
                            <p><span>5</span> likes</p>
                        </div>
                    </div>`;

let answer = `<div class="answer-comment">
                        <p><span>currentUser</span> comment:</p>
                        <div class="answer">
                            <form>
                                <textarea name="postText" id="comment" cols="30" rows="10"></textarea>
                                <div>
                                    <label for="username">Username <span class="red">*</span></label>
                                    <input type="text" name="username" id="username">
                                </div>
                                <button>Post</button>
                            </form>
                        </div>
                    </div>`;


function solve() {
    let sectionPostForm = document.getElementById('postComment');
    document.getElementsByTagName('a')[0].addEventListener('click', reload)
    sectionPostForm.innerHTML = loadPostForm();
    document.getElementById('postPost').addEventListener('submit', createPost);
    loadPosts();
}

solve();
function reload(){
    solve()
}

async function createPost(event) {
    event.preventDefault();
    let form = event.target;
    let formData = new FormData(form);
    let post = {
        title: formData.get('topicName'),
        username: formData.get('username'),
        text: formData.get('postText'),
        date: new Date(),
        subscribers: Math.floor(Math.random() * 500)

    };
    if (post.title === '' || post.username === '' || post.text === '') {
        return alert('All fields are required!');
    }
    await fetch('http://localhost:3030/jsonstore/collections/myboard/posts', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(post)
    });
    form.getElementsByClassName('cancel')[0].addEventListener('click',()=>form.reset())
    form.reset();
    loadPosts();

}

function loadPostForm() {
    let postForm = `<div class="new-topic-border">
                <div class="header-background">
                    <span>New Topic</span>
                </div>
                <form id="postPost">
                    <div class="new-topic-title">
                        <label for="topicName">Title <span class="red">*</span></label>
                        <input type="text" name="topicName" id="topicName">
                    </div>
                    <div class="new-topic-title">
                        <label for="username">Username <span class="red">*</span></label>
                        <input type="text" name="username" id="username">
                    </div>
                    <div class="new-topic-content">
                        <label for="postText">Post <span class="red">*</span></label>
                        <textarea type="text" name="postText" id="postText" rows="8" class="height"></textarea>
                    </div>
                    <div class="new-topic-buttons">
                        <button class="cancel">Cancel</button>
                        <button class="public">Post</button>
                    </div>

                </form>
            </div>`;
    return postForm;
}

async function getPosts() {
    let response = await fetch('http://localhost:3030/jsonstore/collections/myboard/posts');
    let data = await response.json();
    return data;
}

async function loadPosts() {
    let posts = await getPosts();
    let sectionPosts = document.getElementById('postedContent');
    sectionPosts.innerHTML = ''
    for (const post of Object.values(posts)) {
        let postContent = `
                <!-- topic component  -->
                <div class="topic-container">
                    <div class="topic-name-wrapper">
                        <div class="topic-name">
                            <a id = "titleLink" href="#" class="normal" onClick>
                                <h2>${post.title}</h2>
                            </a>
                            <div class="columns">
                                <div>
                                    <p>Date:
                                        <time>${post.date}</time>
                                    </p>
                                    <div class="nick-name">
                                        <p>Username: <span>${post.username}</span></p>
                                    </div>
                                </div>
                                <div class="subscribers">
                                    <!-- <button class="subscribe">Subscribe</button> -->
                                    <p>Subscribers: <span>${post.subscribers}</span></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>`;
        let div = document.createElement('div');
        div.className = 'topic-title';
        div.innerHTML = postContent;
        sectionPosts.appendChild(div);
    }
}
