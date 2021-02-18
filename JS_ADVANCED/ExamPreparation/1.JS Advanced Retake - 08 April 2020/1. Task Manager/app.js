function solve() {

    let task = document.getElementById('task')
    let description = document.getElementById('description')
    let dueDate = document.getElementById('date')
    let addButton = document.getElementById('add');
    let openTasks = document.getElementsByTagName('section')[1].children[1]
    let inProgress = document.getElementById("in-progress")
    let completed = document.getElementsByTagName('section')[3].children[1]
    document.getElementsByTagName('body')[0].addEventListener('click', clickHandler);


    function clickHandler(event) {
        event.preventDefault();
        if (event.target === addButton && task.value !== '' && description.value !== '' && dueDate.value !== '') {
            createArticle()
        }
        if (event.target.className === 'red'){
            let article = event.target.parentElement.parentElement
            deleteArt(article)
        }

        if (event.target.className === 'green'){
            let article = event.target.parentElement.parentElement
            move(article)
        }
        if (event.target.className === 'orange'){
            let article = event.target.parentElement.parentElement
            finish(article)
        }

    }
    function deleteArt(article){
        let div = article.parentElement;
        div.removeChild(article)
    }


    function finish(article){
        inProgress.removeChild(article)
        completed.appendChild(article)
        let div = article.children[3]
        article.removeChild(div)


    }

    function move(article){
        openTasks.removeChild(article)
        inProgress.appendChild(article)
        let div = article.children[3]
        div.removeChild(div.firstChild)
        let finishButton = document.createElement('button')
        finishButton.className='orange'
        finishButton.textContent = 'Finish'
        div.appendChild(finishButton)


    }
    function createArticle(){
        let article = document.createElement('article')
        let h3 = document.createElement('h3')
        h3.innerHTML = task.value
        let pDescription = document.createElement('p')
        pDescription.innerHTML = 'Description: '+description.value
        let pDue = document.createElement('p')
        pDue.innerHTML = 'Due Date: '+dueDate.value
        let div = document.createElement('div')
        div.className = 'flex'
        let startButton = document.createElement('button')
        startButton.className = 'green'
        startButton.innerHTML = 'Start'
        let deleteButton = document.createElement('button')
        deleteButton.className = 'red'
        deleteButton.innerHTML = 'Delete'
        article.appendChild(h3)
        article.appendChild(pDescription)
        article.appendChild(pDue)
        div.appendChild(startButton)
        div.appendChild(deleteButton)
        article.appendChild(div)
        openTasks.appendChild(article)
    }
}