function solution() {
    document.getElementsByTagName('body')[0].addEventListener('click', listener);
    let textBox = document.getElementsByTagName('input')[0];
    let button = document.getElementsByTagName('button')[0];
    let listOfGiftsCardUl = document.getElementsByClassName('card')[1].children[1];
    let sendGiftsCardUl = document.getElementsByClassName('card')[2].children[1];
    let discardedGiftsCardUl = document.getElementsByClassName('card')[3].children[1];

    function listener(event) {
        if (event.target === button) {
            addItemToGiftList();
        }

        if (event.target.textContent === document.getElementsByClassName('sendButton')[0].textContent) {
            let element = event.target;
            send(element);
        }
        if (event.target.textContent === document.getElementsByClassName('discardButton')[0].textContent) {
            let element = event.target;
            discard(element);
        }
    }

    function send(element) {
        let li = element.parentElement;
        listOfGiftsCardUl.removeChild(li);
        let b1 = li.children[0];
        let b2 = li.children[1];
        li.removeChild(b1);
        li.removeChild(b2);
        sendGiftsCardUl.appendChild(li);
    }

    function discard(element) {
        let li = element.parentElement;
        listOfGiftsCardUl.removeChild(li);
        let b1 = li.children[0];
        let b2 = li.children[1];
        li.removeChild(b1);
        li.removeChild(b2);
        discardedGiftsCardUl.appendChild(li);
    }

    function addItemToGiftList() {
        if (textBox.value !== '') {
            listOfGiftsCardUl.appendChild(createLi());
            sort();
        }
    }

    function createLi() {
        let li = document.createElement('li');
        li.textContent = textBox.value;
        li.className = 'gift';
        let sendButton = document.createElement('button');
        sendButton.innerHTML = 'Send';
        sendButton.className = 'sendButton';
        li.appendChild(sendButton);
        let discardButton = document.createElement('button');
        discardButton.innerHTML = 'Discard';
        discardButton.className = 'discardButton';
        li.appendChild(discardButton);
        textBox.value = '';
        return li;
    }

    function sort() {
        let lis = listOfGiftsCardUl.children;
        let unsorted = Array.from(lis);
        let sortedLis = unsorted.sort((a, b) => a.innerHTML.localeCompare(b.innerHTML));
        if (lis.length > 1) {
            for (let i = 0; i < unsorted.length; i++) {
                listOfGiftsCardUl.appendChild(sortedLis[i]);
            }
        }
    }
}

//Victrors first solution
// function solution() {
//     // attach event listeners to input form
//     const [gifts, sent, discarded] = document.querySelectorAll('section ul');
//     const input = document.querySelector('input');
//     document.querySelector('button').addEventListener('click', addGift);
//
//     // create gift elements with buttons
//     function addGift() {
//         const name = input.value;
//         input.value = '';
//
//         const element = e('li', name, 'gift');
//         const sendBtn = e('button', 'Send', 'sendButton');
//         const discardBtn = e('button', 'Discard', 'discardButton');
//         element.appendChild(sendBtn);
//         element.appendChild(discardBtn);
//
//         sendBtn.addEventListener('click', () => sendGift(name, element));
//         discardBtn.addEventListener('click', () => discardGift(name, element));
//
//         gifts.appendChild(element);
//
//         sortGifts();
//     }
//
//     // logic for sending gifts
//     function sendGift(name, gift) {
//         gift.remove();
//         const element = e('li', name, 'gift');
//         sent.appendChild(element);
//     }
//
//     // logic for discarding gifts
//     function discardGift(name, gift) {
//         gift.remove();
//         const element = e('li', name, 'gift');
//         discarded.appendChild(element);
//     }
//
//     // sort gifts list
//     function sortGifts() {
//         Array
//             .from(gifts.children)
//             .sort((a, b) => a.childNodes[0].textContent.localeCompare(b.childNodes[0].textContent))
//             .forEach(g => gifts.appendChild(g));
//     }
//
//     function e(type, content, className) {
//         const result = document.createElement(type);
//         result.textContent = content;
//         if (className) {
//             result.className = className;
//         }
//         return result;
//     }
// }

//Victors Refactured

// function solution() {
//     const [gifts, sent, discarded] = document.querySelectorAll('section ul');
//     const input = document.querySelector('input');
//     document.querySelector('button').addEventListener('click', addGift);
//
//     function addGift() {
//         const name = input.value;
//         input.value = '';
//
//         const element = e('li', name, 'gift');
//         element.giftName = name;
//         const sendBtn = e('button', 'Send', 'sendButton', () => dispatchGift(sent, name, element));
//         const discardBtn = e('button', 'Discard', 'discardButton', () => dispatchGift(discarded, name, element));
//         element.appendChild(sendBtn);
//         element.appendChild(discardBtn);
//
//
//         let inserted = false;
//         for (let child of Array.from(gifts.children)) {
//             if (child.textContent.localeCompare(element.textContent) == 1) {
//                 gifts.insertBefore(element, child);
//                 inserted = true;
//                 break;
//             }
//         }
//         if (!inserted) {
//             gifts.appendChild(element);
//         }
//     }
//
//     function dispatchGift(target, name, gift) {
//         gift.remove();
//         const element = e('li', name, 'gift');
//         target.appendChild(element);
//     }
//
//     function e(type, content, className, onClick) {
//         const result = document.createElement(type);
//         result.textContent = content;
//         if (className) {
//             result.className = className;
//         }
//         if (onClick) {
//             result.addEventListener('click', onClick);
//         }
//         return result;
//     }
// }