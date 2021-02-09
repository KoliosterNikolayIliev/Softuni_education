let {assert} = require('chai')
let lookupChar = require('../03.CharLookup')

describe('test output', ()=>{
    it('checks input values',()=>{
        assert.isUndefined(lookupChar(1,1))
        assert.isUndefined(lookupChar(1,'1'))
        assert.isUndefined(lookupChar('1',1.2))
    })
    it('checks indexes',()=>{
        assert.equal(lookupChar('12',3), "Incorrect index")
        assert.equal(lookupChar('12',2), "Incorrect index")
        assert.equal(lookupChar('12',-1), "Incorrect index")
    })

    it('checks for correct output',()=>{
        assert.equal(lookupChar('12',0), "1")
    })
    it('',()=>{
        assert.equal(lookupChar('abv',0), "a")
        assert.equal(lookupChar('abv',2), "v")
    })

})