function jsonToHtml(json) {
    let arr = JSON.parse(json);

    let outputArr = ["<table>"];
    outputArr.push(makeKeyRow(arr));
    arr.forEach((obj) => outputArr.push(makeValueRow(obj)));
    outputArr.push("</table>");

    function makeKeyRow(arr) {
        let keys = [];
        for (const el of Object.keys(arr[0])) {
            keys.push(el);
        }
        return keys;
    }

    function makeValueRow(obj) {
        let values = [];
        for (const key in obj) {
            values.push(obj[key]);
        }
        return values;
    }

    function escapeHtml(value) {
        if (typeof value === "string"){
            value = value.replace(/&/g, '&amp;') .replace(/</g, '&lt;') .replace(/>/g, '&gt;') .replace(/"/g, '&quot;') .replace(/'/g, '&#39;');
        }
        // let newV;
        // const specials = {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'};
        //     for (const spec in specials) {
        //         if (value.toString().includes(spec)) {
        //             newV = value.replace(value[value.indexOf(spec)], specials[spec]);
        //             value = newV
        //         }
        //     }
        return value;
    }

    let begin = outputArr.shift();
    let end = outputArr.pop();
    // console.log(outputArr);
    let b = outputArr.shift().map(el => escapeHtml(el));
    let result1 = '\n' + '<tr><th>' + b.join('</th><th>') + '</th></tr>';
    let result2 = '';
    for (let i = 0; i < outputArr.length; i++) {
        let a = outputArr[i].map(el => escapeHtml(el));
        result2 += '\n' + '<tr><td>' + a.join('</td><td>') + '</td></tr>';
    }


    return begin + result1 + result2 + '\n' + end;

}

console.log(jsonToHtml('[{"<&Name":"&Stamat","Score":5.5},{"Name":"Rumen","Score":6}]'));
// console.log(jsonToHtml('[{"<Name":"&Pesho","<Score":4,"&Grade":8},{"Name":"Gosho","Score":5," &Grade":8},{"Name":"Angel","Score":5.50,"&&Grade":10}]'));