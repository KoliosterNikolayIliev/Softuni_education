async function lockedProfile() {
    await loadProfiles()
    let profiles = Array.from(document.getElementsByClassName('profile'));

    for (let profile of profiles) {
        profile.addEventListener('click', showHide);
        profile.addEventListener('click', lockUnlock);
    }

    function showHide(event) {
        if (event.target.tagName === 'BUTTON') {
            let button = event.target;
            if(button.parentElement.getElementsByTagName('input')[0].checked===true){
                button.disabled = "true"
                return
            }else {button.disabled = false}
            if (button.textContent === 'Show more') {
                button.textContent = 'Hide it';
                button.parentElement.getElementsByTagName('div')[0].style.display = 'block';
            } else {
                button.textContent = 'Show more';
                button.parentElement.getElementsByTagName('div')[0].style.display = 'none';
            }

        }
    }

    function lockUnlock(event) {
        if (event.target.tagName === 'INPUT') {
            if (event.target.value === 'lock') {
                event.target.parentElement.getElementsByTagName('button')[0].disabled = true;
            }else {
                event.target.parentElement.getElementsByTagName('button')[0].disabled = false;
            }
        }
    }
}

async function loadProfiles(){
    let url = 'http://localhost:3030/jsonstore/advanced/profiles'
    let response = await fetch(url)
    let data = await response.json()
    let main = document.getElementById('main')
    let counter = 1
    for (const item of Object.values(data)) {
        let divProfile = createEl('div','','','','','profile')
        main.appendChild(divProfile)
        let img = createEl('img',"./iconProfile2.png",'','', '','userIcon')
        divProfile.appendChild(img)
        let labelL = createEl('label', '', '', '', '', '', '', 'Lock')
        divProfile.appendChild(labelL)
        let inputRadioOne = createEl('input','', `user${counter}Locked`,'lock','radio','','','', '','', )
        divProfile.appendChild(inputRadioOne)
        let labelU = createEl('label', '', '', '', '', '', '', 'Unlock')
        divProfile.appendChild(labelU)
        let inputRadioTwo = createEl('input','', `user${counter}Locked`,'unlock','radio','','','','','',)
        divProfile.appendChild(inputRadioTwo)
        divProfile.appendChild(document.createElement('br'))
        divProfile.appendChild(document.createElement('hr'))
        let labelUn = createEl('label', '', '', '', '', '', '', 'Username')
        divProfile.appendChild(labelUn)
        let inputUser = createEl('input','',`user${counter}Username`,item.username,'text', '', '', '', 'disabled','readonly')
        divProfile.appendChild(inputUser)
        let divHidden = createEl('div', '', '', '', '', '', `user${counter}HiddenFiles`)
        divHidden.style.display = 'none'
        divProfile.appendChild(divHidden)
        divHidden.appendChild(document.createElement('hr'))
        let labelMail = createEl('label', '', '', '', '', '', '', 'Email:')
        divHidden.appendChild(labelMail)
        let inputMail = createEl('input','', `user${counter}Email`,item.email,'email','', '', '', 'disabled', 'readonly')
        divHidden.appendChild(inputMail)
        let labelAge = createEl('label', '', '', '', '', '', '', 'Age:')
        divHidden.appendChild(labelAge)
        let inputAge = createEl('input','', `user${counter}Age`,item.age,'email','', '', '', 'disabled', 'readonly')
        divHidden.appendChild(inputAge)
        let showMoreBtn = createEl('button','','', '', '', '', '', 'Show more')
        divProfile.appendChild(showMoreBtn)
        counter++
        inputRadioOne.checked = true
    }
}

/*
<div class="profile">
				<img src="./iconProfile2.png" class="userIcon" />
				<label>Lock</label>
				<input type="radio" name="user1Locked" value="lock" checked>
				<label>Unlock</label>
				<input type="radio" name="user1Locked" value="unlock"><br>
				<hr>
				<label>Username</label>
				<input type="text" name="user1Username" value="" disabled readonly />
				<div id="user1HiddenFields">
					<hr>
					<label>Email:</label>
					<input type="email" name="user1Email" value="" disabled readonly />
					<label>Age:</label>
					<input type="email" name="user1Age" value="" disabled readonly />
				</div>
				<button>Show more</button>
			</div>
 */

function createEl(elType, src, name, value, type, elClass, id, content, disabled, readonly){
    let el = document.createElement(elType)
    if (elClass){el.className = elClass}
    if (id){el.id = id}
    if (content){el.innerHTML = content}
    if(src){el.src = src}
    if(type){el.type = type}
    if (name){el.name = name}
    if (value){el.value = value}
    if (disabled){el.disabled = true}
    if (readonly){el.readOnly = true}
    return el
}