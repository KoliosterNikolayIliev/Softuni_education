function solve() {
    let lectureName = document.getElementsByClassName('form-control')[0].children[1];
    let date = document.getElementsByClassName('form-control')[1].children[1];
    let module = document.getElementsByClassName('form-control')[2].children[1];
    let add = document.getElementsByClassName('form-control')[3].children[0];
    let modules = document.getElementsByClassName('modules')[0];


    add.addEventListener('click', addLectureOrModule);

    function addLectureOrModule(event) {
        event.preventDefault();
        if (lectureName.value !== '' && date.value !== '' && module.value !== "Select module") {
            addLecture();

        }

        function addModule() {
            let newModule = createEl('div', '', 'module');
            let h3 = createEl('h3', module.value.toUpperCase() + '-' + 'MODULE');
            newModule.appendChild(h3);
            let ul = createEl('ul');
            newModule.appendChild(ul);
            return newModule;
        }

        function addLecture() {
            let li = createEl('li', '', 'flex');
            let dateSplit = date.value.split('T');
            let formatedDate = dateSplit[0].split('-').join('/') + ' - ' + dateSplit[1];
            let h4 = createEl('h4', lectureName.value + ' - ' + formatedDate);
            let button = createEl('button', 'Del', 'red');
            button.addEventListener('click', deleteFn)
            li.appendChild(h4);
            li.appendChild(button);
            let newModule = Array.from(modules.children).find(mod => mod.firstChild.textContent === module.value.toUpperCase() + '-' + 'MODULE');
            console.log(newModule);
            if (newModule!==undefined) {
                newModule.children[1].appendChild(li);
            }else{
                newModule = addModule();
                newModule.children[1].appendChild(li);
                modules.appendChild(newModule);
            }
            sort()
        }
        function deleteFn(event){
            let li = event.target.parentElement
            let ul = li.parentElement
            let div = ul.parentElement
            let mainDiv = div.parentElement
            if(ul.childElementCount===1){
                mainDiv.removeChild(div)
            }else{
                ul.removeChild(li)
            }
        }
        function sort(){
            let collection = Array.from(modules.children)
                for (let div of collection){
                    for(let ul of Array.from(div.children)){
                        let licol = Array.from(ul.children)
                        let sortedli = licol.sort((a,b)=>a.children[0].textContent.localeCompare(b.children[0].textContent))
                        for (let i = 0; i < licol.length; i++) {
                            licol[i].parentElement.appendChild(sortedli[i])
                        }
                    }
                }
        }

        function createEl(type, content, className) {
            const result = document.createElement(type);
            if (content) {
                result.textContent = content;
            }
            if (className) {
                result.className = className;
            }
            return result;
        }
    }
}

