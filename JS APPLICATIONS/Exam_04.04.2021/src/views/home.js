import {html} from '../lib.js'
import {getHomeItems} from '../api/data.js';
import {homeItemTemplate} from './common/homeItem.js';

let homeTemplate = (data) => html`
    <section id="home-page" class="content">
        <h1>Recent Articles</h1>
        <section class="recent js">
            <h2>JavaScript</h2>
            ${(data.filter(item => item.category==='JavaScript')).length>0?homeItemTemplate(data.filter(item => item.category==='JavaScript')[0]):html`<h3 class="no-articles">No articles yet</h3>`}
        </section>
        <section class="recent csharp">
            <h2>C#</h2>
            ${(data.filter(item => item.category==='C#')).length>0?homeItemTemplate(data.filter(item => item.category==='C#')[0]):html`<h3 class="no-articles">No articles yet</h3>`}
        </section>
        <section class="recent java">
            <h2>Java</h2>
            ${(data.filter(item => item.category==='Java')).length>0?homeItemTemplate(data.filter(item => item.category==='Java')[0]):html`<h3 class="no-articles">No articles yet</h3>`}
        </section>
        <section class="recent python">
            <h2>Python</h2>
            ${(data.filter(item => item.category==='Python')).length>0?homeItemTemplate(data.filter(item => item.category==='Python')[0]):html`<h3 class="no-articles">No articles yet</h3>`}
        </section>
    </section>`;



export async function indexPage(context) {

    let data = await getHomeItems()

    context.render(homeTemplate(data))
}