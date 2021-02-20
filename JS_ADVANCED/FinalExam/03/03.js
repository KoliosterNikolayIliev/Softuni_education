const numberOperations = {
    powNumber: function (num) {
        return num * num;
    },
    numberChecker: function (input) {
        input = Number(input);

        if (isNaN(input)) {
            throw new Error('The input is not a number!');
        }

        if (input < 100) {
            return 'The number is lower than 100!';
        } else {
            return 'The number is greater or equal to 100!';
        }
    },
    sumArrays: function (array1, array2) {

        const longerArr = array1.length > array2.length ? array1 : array2;
        const rounds = array1.length < array2.length ? array1.length : array2.length;

        const resultArr = [];

        for (let i = 0; i < rounds; i++) {
            resultArr.push(array1[i] + array2[i]);
        }

        resultArr.push(...longerArr.slice(rounds));

        return resultArr
    }
};


let{assert}=require('chai')

describe("Tests …", function() {
    describe("TODO …", function() {
        it("TODO …", function() {
            assert.equal(numberOperations.powNumber(2),4)
        });
        it("TODO …", function() {
            assert.equal(numberOperations.powNumber(0),0)
        });
        it("TODO …", function() {
            assert.equal(numberOperations.numberChecker(99),'The number is lower than 100!')
        });
        it("TODO …", function() {
            assert.equal(numberOperations.numberChecker(101),'The number is greater or equal to 100!')
        });
        it("TODO …", function() {
            assert.equal(numberOperations.numberChecker(100),'The number is greater or equal to 100!')
        });
        it("TODO …", function() {
            assert.throw(()=>numberOperations.numberChecker('hhh'),'The input is not a number!')
        });

        it("TODO …", function() {
            assert.deepEqual(numberOperations.sumArrays([1,1],[1,1,1]),[ 2, 2, 1 ])
        });

        it("TODO …", function() {
            assert.deepEqual(numberOperations.sumArrays([1,1,1],[1,1]),[ 2, 2, 1 ])
        });

        it("TODO …", function() {
            assert.deepEqual()
        });
        it("TODO …", function() {
            assert.deepEqual()
        });
    });

});

