function attachEvents() {
    document.getElementsByClassName('load')[0].addEventListener('click', getCatches)
}

attachEvents();

async function getCatches(){
    let url = 'http://localhost:3030/data/catches'
    let response = await fetch(url)
    let data = await response.json()
    await loadCatches(data)
}

async function loadCatches(data){
    console.log(data)
    let catches = document.getElementById('catches')
    catches.innerHTML = ''
    let allCatches = []
    for (const fish of data) {
        let catchDiv = `<div id ="${fish._id}" class="catch">
                    <input type="hidden" id = "ownerId" value="${fish._ownerId}">
                    <label>Angler</label>
                    <input type="text" class="angler" value="${fish.angler}" />
                    <hr>
                    <label>Weight</label>
                    <input type="number" class="weight" value="${fish.weight}" />
                    <hr>
                    <label>Species</label>
                    <input type="text" class="species" value="${fish.species}" />
                    <hr>
                    <label>Location</label>
                    <input type="text" class="location" value="${fish.location}" />
                    <hr>
                    <label>Bait</label>
                    <input type="text" class="bait" value="${fish.bait}" />
                    <hr>
                    <label>Capture Time</label>
                    <input type="number" class="captureTime" value="${fish["captureTime "]}" />
                    <hr>
                    <button disabled class="update">Update</button>
                    <button disabled class="delete">Delete</button>
                </div>`
        allCatches.push(catchDiv)
    }
    catches.innerHTML = allCatches.join('\n')

}
