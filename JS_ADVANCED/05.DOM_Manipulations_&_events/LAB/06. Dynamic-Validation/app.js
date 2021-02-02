function validate() {
    document.getElementById('email').addEventListener('change', onChange)

    function onChange(event){
        let email = event.target.value;
        let element = event.target
        if(/^[a-z]+@[a-z]+\.[a-z]+$/.test(email)){
            element.className = ''
        }else{element.className = 'error'}

    }
}