(function solve() {
    String.prototype.ensureStart = function (string) {
        if (!this.valueOf().startsWith(string)) {
            return string + this.valueOf();
        }
        return this.valueOf();
    };
    String.prototype.ensureEnd = function (string) {
        if (!this.valueOf().endsWith(string)) {
            return this.valueOf() + string;
        }
        return this.valueOf();
    };
    String.prototype.isEmpty = function () {
        return this.length === 0;
    };
    String.prototype.truncate = function (n) {
        if (this.length <= n) {
            return this.valueOf();
        }
        if (n < 4) {
            return '.'.repeat(n);
        }
        if (!this.includes(' ')) {
            let result = this.slice(0, n - 3) + '...';
            return result;
        }
        let splitString = this.split(' ');
        let result = splitString[0];

        for (let i = 1; i < splitString.length; i++) {
            if (result.length + splitString[i].length + 4 > n) {
                return result + '...';
            }
            result += ' ' + splitString[i];
        }
        return result;
    };

    String.format = function (string, ...params) {
        return string.replace(/\{([\d]+)\}/g, function (match, group) {
            return params[Number(group)] === undefined ? match : params[Number(group)];
        });
    };
}());
// let str = 'my string';
// str = str.ensureStart('my');
// console.log(str);
// str = str.ensureStart('hello ');
// console.log(str);
// str = str.truncate(16);
// console.log(str);
// str = str.truncate(14);
// console.log(str);
// str = str.truncate(8);
// console.log(str);
// str = str.truncate(4);
// console.log(str);
// str = str.truncate(2);
// console.log(str);
// str = String.format('The {0} {1} fox',
//     'quick', 'brown');
// console.log(str);
// str = String.format('jumps {0} {1}',
//     'dog');
// console.log(str);



