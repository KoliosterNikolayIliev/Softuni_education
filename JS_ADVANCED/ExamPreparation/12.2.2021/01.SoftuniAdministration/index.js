function solve() {
    let lectureName = document.getElementsByClassName('form-control')[0].children[1]
    let date = document.getElementsByClassName('form-control')[1].children[1]
    let module = document.getElementsByClassName('form-control')[2].children[1]
    let modulesCust = document.getElementsByClassName('user-view section-view')[0].children[1]

    document.getElementsByTagName('button')[0].addEventListener('click', myFunction)
    function myFunction(event) {
        event.preventDefault()
        if (lectureName.value!==''&&date.value!==''&&module.value!=='Select module'){
            addModuleOrLecture()
        }
    }
    function createModule(){
        let divModule = document.createElement('div')
        divModule.className = 'module'
        let h3 = document.createElement('h3')
        h3.textContent = module.value.toUpperCase() + '-' + 'MODULE'
        let ul = document.createElement('ul')
        divModule.appendChild(h3)
        divModule.appendChild(ul)
        return divModule
    }
    function createLecture(){
        let li = document.createElement('li')
        li.className = 'flex'
        let h4 = document.createElement('h4')
        let dateArr = date.value.split('-')
        let formattedDate = dateArr[0]+'/'+dateArr[1]+'/'+dateArr[2].slice(0,2)+' - '+dateArr[2].slice(3)
        h4.textContent = lectureName.value + ' '+'-'+' '+formattedDate
        let button = document.createElement('button')
        button.className = 'red'
        button.textContent = 'Del'
        li.appendChild(h4)
        li.appendChild(button)
        button.addEventListener('click',deleteLorM)
        return li
    }

    function addModuleOrLecture(){
        let modulesCol = modulesCust.children
        let modulesArr = Array.from(modulesCol)
        let moduleToAppend = modulesArr.find(mod=>mod.children[0].textContent===module.value.toUpperCase() + '-' + 'MODULE')
        if (moduleToAppend===undefined || modulesCol.childElementCount===0){
            modulesCust.appendChild(createModule())
            modulesCust.lastChild.children[1].appendChild(createLecture())
        }else{
            moduleToAppend.children[1].appendChild(createLecture())
        }
        sort()
    }
    function deleteLorM(event){
        let lecture = event.target.parentElement
        let ul = lecture.parentElement
        let module = ul.parentElement
        if (ul.childElementCount===1){
            module.remove()
        }else{
            lecture.remove()
        }
    }
    function sort(){
        let lis =
        }
    }
}