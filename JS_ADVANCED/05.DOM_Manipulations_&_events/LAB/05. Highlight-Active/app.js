function focus() {
    let mainDiv = Array.from(document.querySelector('div').children);
    for (let div of mainDiv) {
        div.children[1].addEventListener('focus', function (){div.className = 'focused'});
        div.children[1].addEventListener('blur', function (){div.className = 'blurred'});
    }
}

// div.addEventListener('mousemove',function (){})
// div.addEventListener('mouseout',function (){div.style= ''})