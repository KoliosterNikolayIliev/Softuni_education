function solve() {
    let text = document.getElementById('text').value;
    let caseType = document.getElementById('naming-convention').value;
    let endResult = document.getElementById('result');

    const words = text.split(' ').map(el => el.toLowerCase());

    let result = words.map(el => capitalise(el)).join('');

    if (caseType === "Pascal Case") {
        endResult.textContent = result;

    } else if (caseType === "Camel Case") {
        endResult.textContent = result.charAt(0).toLowerCase() + result.slice(1);

    } else {

        endResult.textContent = "Error!";

    }

    function capitalise(text) {
        return text.charAt(0).toUpperCase() + text.slice(1);
    }
}

