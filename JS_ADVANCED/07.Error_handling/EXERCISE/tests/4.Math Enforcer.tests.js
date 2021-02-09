let {assert} = require('chai');

let mathEnforcer = {
    addFive: function (num) {
        if (typeof (num) !== 'number') {
            return undefined;
        }
        return num + 5;
    },
    subtractTen: function (num) {
        if (typeof (num) !== 'number') {
            return undefined;
        }
        return num - 10;
    },
    sum: function (num1, num2) {
        if (typeof (num1) !== 'number' || typeof (num2) !== 'number') {
            return undefined;
        }
        return num1 + num2;
    }
};

describe('Math enforcer', () => {
    describe('addFive', () => {
        it('return correct when input not number and number', () => {
            assert.equal(mathEnforcer.addFive(1),6)
            assert.equal(mathEnforcer.addFive('1'),undefined)
            assert.equal(mathEnforcer.addFive(-1),4)
            assert.closeTo(mathEnforcer.addFive(1.4),6.4,0)
        });
    });
    describe('subtractTen', () => {
        it('return correct when input not number and number', () => {
            assert.equal(mathEnforcer.subtractTen(1),-9)
            assert.equal(mathEnforcer.subtractTen('1'),undefined)
            assert.equal(mathEnforcer.subtractTen(-1),-11)
            assert.closeTo(mathEnforcer.subtractTen(1.4),-8.6,0)
        });
    });
    describe('sum', () => {
        it('return correct when input not number and number', () => {
            assert.equal(mathEnforcer.sum(1,2),3)
            assert.equal(mathEnforcer.sum(-1,2),1)
            assert.equal(mathEnforcer.sum(-1,-2),-3)
            assert.equal(mathEnforcer.sum('1',2),undefined)
            assert.equal(mathEnforcer.sum(1,'2'),undefined)
            assert.closeTo(mathEnforcer.sum(1.2,1.3),2.5,0)
        });
    });
});
