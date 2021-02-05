function solve(array, typeOfSort) {
    if (typeOfSort==='asc'){
        return sortAsc(array)
    }else{
        return sortDsc(array)
    }
    function sortAsc(array) {
        return array.sort(function (a, b) {
            return a - b;
        });
    }

    function sortDsc(array) {
        return array.sort(function (a, b) {
            return b - a;
        });
    }
}

console.log(solve([14, 7, 17, 6, 8], 'asc'))
console.log(solve([14, 7, 17, 6, 8], 'dsc'))