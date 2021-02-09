let {assert} = require('chai');
let rgbToHexColor = require('../07.Error_handling/LAB/06.RGBtoHex');

describe('output RGBtoHEX', () => {
    it('returns string', () => {
        assert.equal(typeof rgbToHexColor(150, 200, 100) == 'string', true);
    });
    it('returns hexColor', () => {
        assert.equal(rgbToHexColor(150, 200, 100) == '#96C864', true);
    });
    it('returns red - value', () => {
        assert.equal(rgbToHexColor(-50, 200, 100), undefined);
    });
    it('returns red big value', () => {
        assert.equal(rgbToHexColor(1000, 200, 100), undefined);
    });
    it('returns green - value', () => {
        assert.equal(rgbToHexColor(150, -50, 100), undefined);
    });
    it('returns green big value', () => {
        assert.equal(rgbToHexColor(150, 260, 100), undefined);
    });
    it('returns blue - value', () => {
        assert.equal(rgbToHexColor(150, 200, -100), undefined);
    });
    it('returns green blue value', () => {
        assert.equal(rgbToHexColor(150, 200, 1000), undefined);
    });
    it('returns undefined if string', () => {
        assert.equal(rgbToHexColor('a', 'b', 'c'), undefined);
    });
    it('black to hex', () => {
        assert.equal(rgbToHexColor(0,0,0), '#000000');
    });
    it('white to hex', () => {
        assert.equal(rgbToHexColor(255,255,255), '#FFFFFF');
    });

});









