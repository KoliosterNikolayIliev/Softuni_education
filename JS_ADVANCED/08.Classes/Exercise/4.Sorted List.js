// let {expect} = require('chai')
//
// class result {
//     constructor() {
//         this.list = [];
//     }
//
//     sortList() {
//         this.list.sort((a, b) => (a - b));
//     }
//
//     add(element) {
//         if (!isNaN(Number(element))) {
//             this.list.push(Number(element));
//             this.sortList();
//         }
//     }
//
//     remove(index) {
//         try {
//             this.list.splice(index, 1);
//             this.sortList();
//         } finally {
//
//         }
//     }
//
//     get(index) {
//         let result = this.list[this.list.length + index];
//
//         if (result !== undefined) {
//             return result;
//         } else {
//             return 'Invalid index'
//         }
//     }
//
//     get size() {
//         return this.list.length;
//     }
// }

class SortedList {
    constructor(list = []) {
        this.list = list.sort((a, b) =>  a - b);
        this.size = this.list.length;
    }

    add(element) {
        this.list.push(element);
        this.list.sort((a, b) => a - b);
        this.size++;
        return;
    }

    remove(index) {
        if (index < 0 || index >= this.list.length) {
            throw new Error(`Index doesn't exist`);
        } else {
            this.list.splice(index, 1);
            this.size--;
            return;
        }
    }

    get(index) {
        if (index < 0 || index >= this.list.length) {
            throw new Error(`Index doesn't exist`);
        } else {
            return this.list[index];
        }
    }
}


// expect(result.prototype.hasOwnProperty('add')).to.equal(true, "Function add() was not found");
// expect(result.prototype.hasOwnProperty('remove')).to.equal(true, "Function remove() was not found");
// expect(result.prototype.hasOwnProperty('get')).to.equal(true, "Function get() was not found");
//
// // Instantiate and test functionality
// var myList = new result();
// expect(myList.hasOwnProperty('size')).to.equal(true, "Property size was not found");
//
// myList.add(5);
// expect(myList.get(0)).to.equal(5, "Element wasn't added");
//
// myList.add(3);
// expect(myList.get(0)).to.equal(3, "Collection wasn't sorted");
//
// myList.remove(0);
// expect(myList.get(0)).to.equal(5, "Element wasn't removed");
// expect(myList.size).to.equal(1, "Element wasn't removed");
