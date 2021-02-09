function validate(httpObj) {
    let validMethods = ['GET', 'POST', 'DELETE', 'CONNECT'];
    let validHTTPVer = ['HTTP/0.9', 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0'];
    let notValidMessage = ['<', '>', '\\', '&', "'", '"'];
    if (!httpObj.method || !validMethods.includes(httpObj.method)) {
        throw new Error(`Invalid request header: Invalid Method`);
    }
    if (!httpObj.uri || !/^(([a-zA-z\d\\.]+)|\*)$/g.test(httpObj.uri)) {
        throw new Error(`Invalid request header: Invalid URI`);
    }
    if (!httpObj.version || !validHTTPVer.includes(httpObj.version)) {
        throw new Error(`Invalid request header: Invalid Version`);
    }
    if (httpObj.message == undefined || httpObj.message.split('').some(r=> notValidMessage.includes(r))) {
        throw new Error(`Invalid request header: Invalid Message`);
    }

    return httpObj;
}

module.exports = validate;


// console.log(validate({
//     method: 'POST',
//     uri: 'home.bash',
//     version: 'HTTP/2.0'
// }));
// console.log(validate({
//         method: 'GET',
//         uri: 'svn.public.catalog',
//         version: 'HTTP/1.1',
//         message: ''
//     }
// ));

// console.log(validate({
//         method: 'OPTIONS',
//         uri: 'git.master',
//         version: 'HTTP/1.1',
//         message: '-recursive'
//     }
// ));
// console.log(validate({
//         method: 'POST',
//         uri: 'home.bash',
//         message: 'rm -rf /*'
//     }
// ));

// console.log(validate({
//     method: 'GET',
//     uri: 'kkk jjjj',
//     version: 'HTTP/0.8',
//     message: ''
// }));
// console.log(validate({
//     method: 'GET',
//     uri: 'svn.public.catalog',
//     version: 'HTTP/1.1',
//     message: 'asl<pls'
// }));


// console.log(validate({}));
console.log(validate({
    method: 'POST',
}));
// console.log(validate({
//     method: 'POST',
//     uri: 'home.bash',
// }));
// console.log(validate({
//     method: 'POST',
//     uri: 'home.bash',
//     version: 'HTTP/2.0'
// }));