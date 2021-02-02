// function solve() {
//     let textAreas = document.querySelectorAll('textarea');
//     let input = textAreas[0];
//     let output = textAreas[1];
//     let table = document.getElementsByTagName('tbody')[0];
//     let bought = {};
//     let factor = [];
//     let furnitureItems;
//     document.getElementsByTagName('button')[0].addEventListener('click', generate);
//     document.getElementsByTagName('button')[1].addEventListener('click', buy);
//
//     function generate() {
//         if (input.value!==''){
//             furnitureItems = JSON.parse(input.value.replace(/'/g,''));
//         }else{
//             return
//         }
//         while (furnitureItems.length > 0) {
//             let forInsert = furnitureItems.shift();
//             let tr = document.createElement('tr');
//
//             let tdImage = document.createElement('td');
//             let img = document.createElement('img');
//             img.src = forInsert['img'];
//             tdImage.appendChild(img);
//             tr.appendChild(tdImage);
//
//             let tdName = document.createElement('td');
//             let nameP = document.createElement('p');
//             nameP.textContent = forInsert['name'];
//             tdName.appendChild(nameP);
//             tr.appendChild(tdName);
//
//             let tdPrice = document.createElement('td');
//             let priceP = document.createElement('p');
//             priceP.textContent = forInsert['price'];
//             tdPrice.appendChild(priceP);
//             tr.appendChild(tdPrice);
//
//             let tdDec = document.createElement('td');
//             let decP = document.createElement('p');
//             decP.textContent = forInsert['decFactor'];
//             tdDec.appendChild(decP);
//             tr.appendChild(tdDec);
//
//             let tdMark = document.createElement('td');
//             let markInput = document.createElement('input');
//             markInput.type = 'checkbox';
//             tdMark.appendChild(markInput);
//             tr.appendChild(tdMark);
//
//             table.appendChild(tr);
//         }
//     }
//
//     function buy() {
//         let checkbox = document.querySelectorAll('input');
//
//         for (let checked of checkbox) {
//             if (checked.checked) {
//                 // console.log(checked.parentElement.parentElement);
//                 let name = checked.parentElement.parentElement.children[1].getElementsByTagName('p')[0].textContent;
//                 let price = Number(checked.parentElement.parentElement.children[2].getElementsByTagName('p')[0].textContent);
//                 let dFactor = Number(checked.parentElement.parentElement.children[3].getElementsByTagName('p')[0].textContent);
//                 bought[name] = price;
//                 factor.push(dFactor);
//             }
//         }
//         if (factor.length > 0) {
//             let totalPrice = Object.values(bought).reduce((accumulator, currentValue) => accumulator + currentValue);
//             let average = (factor.reduce((accumulator, currentValue) => accumulator + currentValue)) / factor.length;
//             output.value = `Bought furniture: ${Object.keys(bought)}` + '\n'
//                 + `Total price: ${totalPrice.toFixed(2)}` + '\n'
//                 + `Average decoration factor: ${average}`;
//         }
//     }
// }

function solve() {

    let [inputBtn, outputBtn] = [...document.querySelectorAll('button')]
    let [inputText, output] = [...document.querySelectorAll('textarea')]

    inputBtn.addEventListener('click', () => {
        let convertInput = JSON.parse(inputText.value);
        convertInput.forEach(e => {
            let {name, img, price, decFactor} = e;

            let html = `<tr>\n
            <td><img src="${img.toString()}"></td>\n
            <td><p>${name}</p></td>\n
            <td><p>${price}</p></td>\n
            <td><p>${decFactor}</p></td>\n
            <td><input type="checkbox"></td>\n
            </tr>\n`

            document.querySelectorAll('tbody')[0].insertAdjacentHTML("beforeend", html)
        });

    });

    outputBtn.addEventListener('click', () => {
        let [products,prices,factors] = [[],[],[]];
        [...document.querySelectorAll('tbody tr')].forEach(tr =>{
            if(tr.querySelectorAll('input')[0].checked){
                let data = tr.querySelectorAll('p');
                products.push(data[0].textContent);
                prices.push(Number(data[1].textContent));
                factors.push(Number(data[2].textContent));
            }
        })

        let names = products.join(', ');
        let totalPrice = prices.reduce((sum, num) => sum + num,0);
        let avg = factors.reduce(function(acc, val) { return acc + val; }, 0)/factors.length;
        output.textContent = `Bought furniture: ${names}\nTotal price: ${totalPrice.toFixed(2)}\nAverage decoration factor: ${avg}`;
    });

}
