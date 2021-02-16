let {assert} = require('chai');

class PaymentPackage {
    constructor(name, value) {
        this.name = name;
        this.value = value;
        this.VAT = 20;      // Default value
        this.active = true; // Default value
    }

    get name() {
        return this._name;
    }

    set name(newValue) {
        if (typeof newValue !== 'string') {
            throw new Error('Name must be a non-empty string');
        }
        if (newValue.length === 0) {
            throw new Error('Name must be a non-empty string');
        }
        this._name = newValue;
    }

    get value() {
        return this._value;
    }

    set value(newValue) {
        if (typeof newValue !== 'number') {
            throw new Error('Value must be a non-negative number');
        }
        if (newValue < 0) {
            throw new Error('Value must be a non-negative number');
        }
        this._value = newValue;
    }

    get VAT() {
        return this._VAT;
    }

    set VAT(newValue) {
        if (typeof newValue !== 'number') {
            throw new Error('VAT must be a non-negative number');
        }
        if (newValue < 0) {
            throw new Error('VAT must be a non-negative number');
        }
        this._VAT = newValue;
    }

    get active() {
        return this._active;
    }

    set active(newValue) {
        if (typeof newValue !== 'boolean') {
            throw new Error('Active status must be a boolean');
        }
        this._active = newValue;
    }

    toString() {
        const output = [
            `Package: ${this.name}` + (this.active === false ? ' (inactive)' : ''),
            `- Value (excl. VAT): ${this.value}`,
            `- Value (VAT ${this.VAT}%): ${this.value * (1 + this.VAT / 100)}`
        ];
        return output.join('\n');
    }
}


describe('Payment package test ', function () {
    let test_instance = undefined;
    beforeEach(function () {
        test_instance = new PaymentPackage('test_name', 100);
    });
    it('constructor', function () {
        assert(Object(test_instance.hasOwnProperty('_name')), true);
        assert.equal(test_instance.value, 100);
        assert.equal(test_instance.VAT, 20);
        assert.equal(test_instance.active, true);
        assert.equal(test_instance.name, 'test_name');
        assert.equal(test_instance._value, 100);
        assert.equal(test_instance._VAT, 20);
        assert.equal(test_instance._active, true);
    });
    it('name', function () {
        assert.equal(test_instance.name, 'test_name');
        test_instance.name = 'Pesho';
        assert.equal(test_instance.name, 'Pesho');
        assert.throw(function () {
            return test_instance.name = '';
        }, 'Name must be a non-empty string');
        assert.throw(function () {
            return test_instance.name = 2;
        }, 'Name must be a non-empty string');
    });
    it('value', function () {
        assert.equal(test_instance.value, 100);
        test_instance.value = 10;
        assert.equal(test_instance.value, 10);
        assert.throw(function () {
            return test_instance.value = '';
        }, 'Value must be a non-negative number');
        assert.throws(function () {
            return test_instance.value = -2;
        }, Error, 'Value must be a non-negative number');
        assert.doesNotThrow(function () {
            test_instance.value = 0;
        });
    });

    it('VAT', function () {
        assert.equal(test_instance.VAT, 20);
        test_instance.VAT = 40;
        assert.equal(test_instance.VAT, 40);
        assert.throw(function () {
            return test_instance.VAT = -2;
        }, 'VAT must be a non-negative number');
        assert.throw(function () {
            return test_instance.VAT = 'test';
        }, 'VAT must be a non-negative number');
    });
    it('active', function () {
        assert.equal(test_instance.active, true);
        test_instance.active = false;
        assert.equal(test_instance.active, false);
        assert.throw(function () {
            return test_instance.active = '';
        }, 'Active status must be a boolean');
        assert.throw(function () {
            return test_instance.active = -2;
        }, 'Active status must be a boolean');
    });
    it('toString', function () {
        function getString(name, value, VAT = 20, active = true) {
            return [
                `Package: ${name}` + (active === false ? ' (inactive)' : ''),
                `- Value (excl. VAT): ${value}`,
                `- Value (VAT ${VAT}%): ${value * (1 + VAT / 100)}`
            ].join('\n');
        }

        assert.equal(test_instance.toString(), getString('test_name', 100));
        test_instance.active = false;
        assert.equal(test_instance.toString(), getString('test_name', 100, 20, false));
        test_instance.VAT = 200;
        assert.equal(test_instance.toString(), getString('test_name', 100, 200, false));
        test_instance.name = 'Toshko';
        assert.equal(test_instance.toString(), getString('Toshko', 100, 200, false));

    });
});


