function solve() {
    document.querySelector('.shopping-cart').addEventListener('click', addItem);
    let textArea = document.getElementsByTagName('textarea')[0];
    let product;
    // let products = document.getElementsByClassName('product')
    let productPrices = {};
    // for (let product of products){
    //     let listItem;
    //     let price;
    //     for (let item of product.children){
    //         if (item.className === 'product-details'){
    //             listItem = item.children[0].textContent
    //         }
    //         if (item.className === 'product-line-price'){
    //             price = Number(item.textContent)
    //         }
    //         if (listItem !== undefined && price !== undefined){
    //             productPrices.push([listItem,price])
    //         }
    //     }
    //
    // }
    // console.log(productPrices);


    function addItem(event) {
        if (event.target.tagName === 'BUTTON' && event.target.className === 'add-product') {
            product = event.target.parentElement.parentElement.children;
            let name = product[1].children[0].textContent;
            let price = Number(product[3].textContent);
            if (productPrices[name]) {
                productPrices[name] += price;
            } else {
                productPrices[name] = price;
            }
            textArea.innerHTML+= `Added ${name} for ${price.toFixed(2)} to the cart.\n`;
        }
        let productList = Object.keys(productPrices).join(', ')
        let totalPrice = Number(Object.values(productPrices).reduce((accumulator, currentValue) => accumulator + currentValue,0))
        if (event.target.tagName === 'BUTTON' && event.target.className === 'checkout') {
            textArea.innerHTML+=`You bought ${productList} for ${totalPrice.toFixed(2)}.`
            let buttons = document.querySelectorAll('button');
            for(let button of buttons){
                button.disabled = true
            }
        }

    }
}