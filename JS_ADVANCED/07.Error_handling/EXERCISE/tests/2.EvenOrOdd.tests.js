let {assert} = require('chai');
let isOddOrEven = require('../2.EvenOrOdd');

describe('tests even odd', () => {
    it('tests input type', () => {
        assert.equal(isOddOrEven(20), undefined)
    });
    it('tests odd', () => {
        assert.equal(isOddOrEven('20'), 'even')
    });
    it('tests even', () => {
        assert.equal(isOddOrEven('201'), 'odd')
    });
});