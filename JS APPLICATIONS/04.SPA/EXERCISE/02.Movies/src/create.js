import {showDetails} from './details.js';

let main;
let section;

export function setupCreate(mainTarget, sectionTarget) {
    main = mainTarget;
    section = sectionTarget;

    let form = section.getElementsByTagName('form')[0];
    form.addEventListener('submit', onSubmit);
}

export async function showCreate() {
    main.innerHTML = '';
    main.appendChild(section);
}

async function onSubmit(event) {
    event.preventDefault();
    let formData = new FormData(event.target);
    let movie = {
        title: formData.get('title'),
        description: formData.get('description'),
        img: formData.get('imageUrl'),
    };
    if (movie.title === '' || movie.description === '' || movie.img === '') {
        return alert('All fields are required!');
    }
    let response = await fetch('http://localhost:3030/data/movies', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
            'X-Authorization': sessionStorage.getItem('authToken')
        },
        body: JSON.stringify(movie)
    });
    if (response.ok) {
        let movie = await response.json();
        showDetails(movie._id);
    } else {
        let error = await response.json();
        alert(error.message);
    }

}