let main;
let section;

export function setupLogin(mainTarget, sectionTarget) {
    main = mainTarget;
    section = sectionTarget;
    let form = section.getElementsByTagName('form')[0];
    form.addEventListener('submit', (event) => {
        event.preventDefault();
    });
}

export async function showLogin() {
    main.innerHTML = '';
    main.appendChild(section);
}