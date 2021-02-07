// function solve() {
//     function solve() {
//         const formElements = document.querySelector('#container').children;
//         const inputs = Array.from(formElements).slice(0, formElements.length - 1);
//         const onScreenBtn = Array.from(formElements).slice(formElements.length - 1)[0];
//         const moviesUl = document.querySelector('#movies>ul');
//         const archiveUl = document.querySelector('#archive>ul');
//         const clearBtn = document.querySelector('#archive>button');
//
//         function clear(e) {
//             e.target.parentNode.innerHTML = "";
//         }
//
//         function archive(e) {
//             const li = e.target.parentNode.parentNode;
//             const div = e.target.parentNode;
//             const input = div.children[1];
//
//             if (Number(input.value) == '') {
//                 return;
//             }
//
//             const span = document.createElement('span');
//             const name = li.children[0].textContent;
//             span.textContent = name;
//
//             const strong = document.createElement('strong');
//             const price = +div.children[0].textContent;
//             const totalPrice = price * Number(input.value);
//             strong.textContent = `Total amount: ${totalPrice.toFixed(2)}`;
//
//             const deleteBtn = document.createElement('button');
//             deleteBtn.textContent = 'Delete';
//             deleteBtn.addEventListener('click', (e) => {
//                 e.target.parentNode.remove();
//             });
//
//             const resultLi = document.createElement('li');
//             resultLi.appendChild(span);
//             resultLi.appendChild(strong);
//             resultLi.appendChild(deleteBtn);
//
//             archiveUl.appendChild(resultLi);
//             li.remove();
//         }
//
//         function createMovie(e) {
//             e.preventDefault();
//
//             const name = inputs[0].value;
//             const hall = inputs[1].value;
//             const price = Number(inputs[2].value);
//
//             if (!name || !hall || !price) {
//                 return;
//             }
//
//             inputs[0].value = "";
//             inputs[1].value = "";
//             inputs[2].value = "";
//
//             const li = document.createElement('li');
//
//             const span = document.createElement('span');
//             span.textContent = name;
//             li.appendChild(span);
//
//             const strong = document.createElement('strong');
//             strong.textContent = `Hall: ${hall}`;
//             li.appendChild(strong);
//
//             const div = document.createElement('div');
//
//             const innerStrong = document.createElement('strong');
//             innerStrong.textContent = price.toFixed(2);
//
//             const input = document.createElement('input');
//             input.setAttribute('placeholder', 'Tickets Sold');
//
//             const archiveBtn = document.createElement('button');
//             archiveBtn.textContent = 'Archive';
//             archiveBtn.addEventListener('click', archive);
//
//             div.appendChild(innerStrong);
//             div.appendChild(input);
//             div.appendChild(archiveBtn);
//
//             li.appendChild(div);
//
//             moviesUl.appendChild(li);
//         }
//
//
//         clearBtn.addEventListener('click', clear);
//         onScreenBtn.addEventListener('click', createMovie);
//     }
// }

// function solve() {
//     const [nameInput, hallInput, priceInput] = document.querySelectorAll('#container input');
//     const moviesUl = document.querySelector('#movies ul');
//     const archiveUl = document.querySelector('#archive ul');
//     moviesUl.innerHTML = '';
//     archiveUl.innerHTML = '';
//     const clearBtn = document.querySelector('#archive button');
//     clearBtn.addEventListener('click', clearMovies);
//     const addBtn = document.querySelector('#container button');
//     addBtn.addEventListener('click', addMovie);
//
//     function clearMovies() {
//         archiveUl.innerHTML = '';
//     }
//
//     function addMovie(e) {
//         e.preventDefault();
//         if (nameInput.value.trim() === '' || hallInput.value.trim() === '' || !Number(priceInput.value)) {
//             return;
//         }
//
//         const li = document.createElement('li');
//         const span = document.createElement('span');
//         span.textContent = `${nameInput.value}`;
//         const strong = document.createElement('strong');
//         strong.textContent = `Hall: ${hallInput.value}`;
//         const div = document.createElement('div');
//         const archiveBtn = document.createElement('button');
//         archiveBtn.textContent = 'Archive';
//         archiveBtn.addEventListener('click', archiveMovie);
//         const strongDiv = document.createElement('strong');
//         strongDiv.textContent = `${Number(priceInput.value).toFixed(2)}`;
//         const input = document.createElement('input');
//         input.placeholder = 'Tickets Sold';
//
//         div.appendChild(strongDiv);
//         div.appendChild(input);
//         div.appendChild(archiveBtn);
//         li.appendChild(span);
//         li.appendChild(strong);
//         li.appendChild(div);
//         moviesUl.appendChild(li);
//
//         nameInput.value = '';
//         hallInput.value = '';
//         priceInput.value = '';
//
//         function archiveMovie(e) {
//
//             if (!Number(input.value)) {
//                 return;
//             }
//
//             strong.textContent = `Total amount: ${(Number(strongDiv.textContent) * Number(input.value)).toFixed(2)}`;
//             const deleteBtn = document.createElement('button');
//             deleteBtn.textContent = 'Delete';
//             deleteBtn.addEventListener('click', deleteMovie);
//             li.appendChild(deleteBtn);
//             archiveUl.appendChild(li);
//
//             div.remove();
//         }
//
//         function deleteMovie() {
//             li.remove();
//         }
//     }
// }



// Solution 100/100 =>

function solve() {
    const data = document.querySelectorAll('#container > input')
    const [name, hall, ticket] = data
    const addBtn = document.querySelector('#container > button')
    const moviesOnScreen = document.querySelector('#movies > ul')
    const archive = document.querySelector('#archive > ul')
    const archiveBtn = document.querySelector('#archive').lastElementChild

    addBtn.addEventListener('click', ctaAddMovie)
    moviesOnScreen.addEventListener('click', ctaArchive)
    archiveBtn.addEventListener( 'click', ctaRemoveArchive)

    function ctaAddMovie(e) {
        e.preventDefault()
        if(name.value === '' || hall.value === '' || !Number(ticket.value)){
            return
        }

        let movie = renderLi('', {}, renderSpan(name.value, {}),
            renderStrong(`Hall: ${hall.value}`, {}),
            renderDiv('', {},
                renderStrong(Number(ticket.value).toFixed(2), {}),
                renderInput('', {'placeholder' : 'Tickets Sold'}),
                renderButton('Archive', {})))

        moviesOnScreen.appendChild(movie)
        Array.from(data).map( x => x.value = '')
    }

    function ctaArchive(e) {
        let ticketSold = e.target.previousElementSibling
        if(e.target.tagName !== 'BUTTON'){
            return
        }
        if(!Number(ticketSold.value) && ticketSold.value !== '0'){
            return
        }
        let liElement = e.target.parentElement.parentElement
        let ticketPrice = Number(liElement.children[2].children[0].textContent)

        liElement.removeChild(liElement.children[2])
        liElement.children[1].textContent = `Total amount: ${(ticketPrice * Number(ticketSold.value)).toFixed(2)}`
        moviesOnScreen.removeChild(liElement)

        const deleteBtn = renderButton('Delete', {})

        deleteBtn.addEventListener('click', e => e.target.parentElement.remove())

        liElement.appendChild(deleteBtn)
        archive.appendChild(liElement)
    }

    function ctaRemoveArchive() {
        Array.from(archive.children).map( x => archive.removeChild(x) )
    }

    const renderLi = renderHtml.bind(undefined, 'li')
    const renderSpan = renderHtml.bind(undefined, 'span')
    const renderStrong = renderHtml.bind(undefined, 'strong')
    const renderDiv = renderHtml.bind(undefined, 'div')
    const renderInput = renderHtml.bind(undefined, 'input')
    const renderButton = renderHtml.bind(undefined, 'button')

    function renderHtml(type, content, attribute, ...children) {
        const element = document.createElement(type)

        if(content !== '' && element.tagName !== 'INPUT'){
            element.innerHTML = content
        }
        if(element.tagName === 'INPUT'){
            element.value = content
        }

        Array.from(children).map( x => element.appendChild(x))
        Object.entries(attribute).map( ([k, v]) => element.setAttribute(k,v))

        return element
    }
}