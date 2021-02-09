const {assert} = require('chai');
const isSymmetric = require('../07.Error_handling/LAB/05.Check for Symmetry');

describe('isSymmetric', () => {
    it('returns true for valid symmetric input', () => {
        assert.equal(isSymmetric([1, 1]), true);
        assert.equal(isSymmetric([1, '1']), false);
    });
    it('throws error for invalid  symmetric input', () => {
        assert.equal(isSymmetric('1',1), false);
    });
    it('throws error for invalid  symmetric input of numbers', () => {
        assert.equal(isSymmetric([2,1]), false);
    });
});



