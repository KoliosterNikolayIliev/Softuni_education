function jsonToHtml(string) {
    let arr = JSON.parse(json);

    let outputArr = ["<table>"];
    outputArr.push(makeKeyRow(arr));
    arr.forEach((obj) => outputArr.push(makeValueRow(obj)));
    outputArr.push("</table>");

    function makeKeyRow(arr) {
    }

    function makeValueRow(obj) {
    }

    function escapeHtml(value) {
    }

    return outputArr.join('\n');
}

console.log(jsonToHtml('[{"Name":"Stamat","Score":5.5},{"Name":"Rumen","Score":6}]'));
console.log(jsonToHtml('[{"Name":"Pesho","Score":4," Grade":8},{"Name":"Gosho","Score":5," Grade":8},{"Name":"Angel","Score":5.50," Grade":10}]'));