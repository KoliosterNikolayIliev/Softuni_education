function solve() {
    let str = '';

    return {append, removeStart, removeEnd, print};

    function append(strApp) {
        str += strApp;
    }

    function removeStart(n) {
        str = str.substring(n);
    }

    function removeEnd(n) {
        str = str.slice(0, -n);
    }

    function print() {
        console.log(str);
    }
}

let firstZeroTest = solve();

firstZeroTest.append('hello');
firstZeroTest.append('again');
firstZeroTest.removeStart(3);
firstZeroTest.removeEnd(4);
firstZeroTest.print();