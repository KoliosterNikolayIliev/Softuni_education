function createSortedList() {
    function sort(arr){
        return arr.sort((a, b) => a - b)
    }
    return {
        size:0,
        arr: [],
        add: function (x) {
            this.arr.push(x);
            this.size++
            return sort(this.arr)
        },
        remove: function (x) {
            if (this.arr[x] !== undefined) {
                this.arr.splice(x, 1);
                this.size--
                return sort(this.arr)
            }
            throw  Error;
        },
        get: function (x) {
            if (this.arr[x] !== undefined) {
                return this.arr[x];
            }
            throw  Error;
        },
    };
}

let list = createSortedList();
list.add(5);
list.add(6);
list.add(7);
console.log(list.get(1));
list.remove(1);
console.log(list.get(1));
