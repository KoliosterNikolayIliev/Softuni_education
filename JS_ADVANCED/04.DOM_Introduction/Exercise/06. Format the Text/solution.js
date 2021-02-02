// function solve() {
//     let text = document.getElementById('input').value.split('.');
//     let output = document.getElementById('output');
//     let formatedText = [];
//     while (text.length > 0) {
//         let sentence = text.shift().trim();
//         if (sentence.length >= 1 && sentence[0] !== ' ') {
//             formatedText.push(sentence + '.');
//         }
//     }
//
//     function createLi() {
//         let li = document.createElement('li');
//         output.appendChild(li);
//         return li
//     }
//
//     let li = createLi();
//     let counter = 0;
//     while (formatedText.length > 0) {
//         let liText = formatedText.shift();
//         li.textContent += liText;
//         counter++;
//         if (counter%3===0){
//             counter = 0
//             li = createLi()
//         }
//     }
// }

// function solve() {
//     let newText = document.getElementById('input').innerText;
//     let sentences = [];
//     sentences = newText.match(/[^\.!\?]+[\.!\?]+/g);
//     let par = [];
//     let cycle = sentences.length;
//     for (let i = 0; i < cycle; i++) {     // Gets every three sentences
//         par[i] = sentences.splice(0, 3).join('');
//     }
//     par = par.filter(item => item);//Removes the empty spaces
//
//     //Bellow selects the output div and appends each element of the array in a new <p>
//     let paragraph = document.getElementById('output');
//     for (let i = 0; i < par.length; i++) {
//         let parHTML = document.createElement('p');
//         parHTML.textContent = par[i];
//         paragraph.appendChild(parHTML);
//     }
// }

function solve() {
    let inputStr = document.getElementById('input').value;
    let output = document.getElementById('output');

    let input = inputStr.split('.').filter((p) => p.length > 0);

    for (let i = 0; i < input.length; i += 3) {
        let arr = [];
        for (let y = 0; y < 3; y++) {
            if (input[i + y]) {
                arr.push(input[i + y]);
            }
        }
        let paragraph = arr.join('. ') + '.';
        output.innerHTML += `<p>${paragraph}</p>`;
    }
}