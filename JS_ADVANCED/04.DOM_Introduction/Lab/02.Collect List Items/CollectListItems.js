function extractText() {
    let elements = document.querySelectorAll("ul#items li")
    let textArea = document.getElementsByTagName('textarea')
    for (let el of elements){
        textArea[0].value+=el.textContent + "\n";
    }

}