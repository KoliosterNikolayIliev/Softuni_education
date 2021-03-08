async function getMovieById(id) {
    let response = await fetch('http://localhost:3030/data/movies/' + id);
    let data = await response.json();
    return data;
}

function createMovieCard(movie) {
    let element = document.createElement('div');
    element.className = 'container';
    element.innerHTML =
        `<div class="container">
                <div class="row bg-light text-dark">
                    <h1>${movie.title}</h1>

                    <div class="col-md-8">
                        <img class="img-thumbnail" src="${movie.img}"
                             alt="Movie">
                    </div>
                    <div class="col-md-4 text-center">
                        <h3 class="my-3 ">Movie Description</h3>
                        <p>${movie.description}</p>
                        <a class="btn btn-danger" href="#">Delete</a>
                        <a class="btn btn-warning" href="#">Edit</a>
                        <a class="btn btn-primary" href="#">Like</a>
                        <span class="enrolled-span">Liked 1</span>
                    </div>
                </div>
            </div>`;
    return element
}

let main;
let section;

export function setupDetails(mainTarget, sectionTarget) {
    main = mainTarget;
    section = sectionTarget;
}

export async function showDetails(id) {
    section.innerHTML = 'Loading&hellip;';
    main.innerHTML = '';
    main.appendChild(section);
    let movie = await getMovieById(id);
    let card = createMovieCard(movie);
    section.innerHTML = ''
    section.appendChild(card);

}