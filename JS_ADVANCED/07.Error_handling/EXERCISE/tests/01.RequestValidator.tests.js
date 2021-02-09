// let {assert, expect} = require('chai');
// let validate = require('../01.RequestValidator');
//
// describe('HTTP object validity tests', () => {
//     it('method, version, uri, message - all valid', () => {
//         let obj = validate({
//                 method: 'GET',
//                 uri: 'svn.public.catalog',
//                 version: 'HTTP/1.1',
//                 message: ''
//             }
//         );
//         assert.equal(validate(obj), obj);
//     });
//     // Make sure regex isn't rejecting valid values
//     let valid = result({
//         method: 'GET',
//         uri: 'svn.public.catalog',
//         version: 'HTTP/1.1',
//         message: ''
//     });
//
//     let obj = {};
//     expect(() => result(obj)).to.throw(Error).which.has.property('message', 'Invalid request header: Invalid Method');
//     obj = {
//         method: 'GET'
//     };
//     expect(() => result(obj)).to.throw(Error).which.has.property('message', 'Invalid request header: Invalid URI');
//     obj = {
//         method: 'GET',
//         uri: 'svn.public.catalog'
//     };
//     expect(() => result(obj)).to.throw(Error).which.has.property('message', 'Invalid request header: Invalid Version');
//     obj = {
//         method: 'GET',
//         uri: 'svn.public.catalog',
//         version: 'HTTP/1.1'
//     };
//     expect(() => result(obj)).to.throw(Error).which.has.property('message', 'Invalid request header: Invalid Message');
//
// });
//
//
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