let {expect, assert} = require('chai');
let sum = require("../07.Error_handling/LAB/01.Sub_SUM");

describe('sum(arr) - sum array of numbers', () => {
    it('should return 3 for [1,2]', function () {
        assert.equal(sum([1, 2]),3);
    });
    it('should return 1 for [1]', function () {
        let expectedSum = 1;
        let actualSum = sum([1]);
        expect(actualSum).to.be.equal(expectedSum);
    });
    it('should return 0 for empty array', function () {
        let expectedSum = 0;
        let actualSum = sum([]);
        expect(actualSum).to.be.equal(expectedSum);
    });
});


