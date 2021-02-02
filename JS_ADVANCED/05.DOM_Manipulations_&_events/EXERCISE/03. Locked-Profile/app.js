function lockedProfile() {
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
                event.target.parentElement.getElementsByTagName('button')[0].disabled = "true";
            }else {
                event.target.parentElement.getElementsByTagName('button')[0].disabled = false;
            }
        }
    }
}
