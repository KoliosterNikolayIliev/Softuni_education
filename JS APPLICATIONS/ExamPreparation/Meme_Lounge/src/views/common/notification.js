
export function notify(message){

    let notification = document.getElementById('errorBox')
    notification.children[0].textContent = message
    let visible = Array.from(document.getElementsByClassName('notification'))

    visible.map(e=>e.style.display = 'inline-block')
    setTimeout(()=>visible.map(e=>e.style.display = 'none'), 3000);
}