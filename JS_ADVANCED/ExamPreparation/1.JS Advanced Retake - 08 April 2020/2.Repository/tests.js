let { Repository } = require("./solution.js");
let{assert}=require('chai')

describe("Tests …", function () {
    let properties = {
        name: "string",
        age: "number",
        birthday: "object"
    };

    describe("Init", function () {
        it("property", function () {
            let repository = new Repository(properties)
            assert.equal(repository.props.toString(), {
                name: "string",
                age: "number",
                birthday: "object"
            })
        });
        it("map", function () {
            let repository = new Repository(properties)
            assert.equal(repository.data.toString(), "[object Map]")
        });
        it("next_id", function () {
            let repository = new Repository(properties)
            assert.equal(repository.nextId(), 0)
            assert.equal(repository.nextId(), 1)
        });
        it("Add", function () {
            let repository = new Repository(properties)
            let entity = {
                name: "Pesho",
                age: 22,
                birthday: new Date(1998, 0, 7)}
            let anotherEntity = {
                name1: 'Stamat',
                age: 29,
                birthday: new Date(1991, 0, 21)
            };
            let anotherEntity2 = {
                name: 'Stamat',
                age: 29,
                birthday: 1991
            };
            let anotherEntity3 = {
                name: 'Stamat',
                age2: 29,
                birthday: new Date(1991, 0, 21)}
            assert.equal(repository.add(entity), 0)
            assert.equal(repository.add(entity), 1)
            assert.throw(function (){repository.add(anotherEntity)},Error,'Property name is missing from the entity!')
            assert.throw(function (){repository.add(anotherEntity2)},Error, `Property birthday is not of correct type!`)
            assert.throw(function (){repository.add(anotherEntity3)},Error,'Property age is missing from the entity!')

        });
        it("Count", function () {
            let repository = new Repository(properties)
            assert.equal(repository.count, 0)
            let entity = {
                name: "Pesho",
                age: 22,
                birthday: new Date(1998, 0, 7)}
            repository.add(entity)
            assert.equal(repository.count, 1)
        });
        it("getID", function () {
            let repository = new Repository(properties)
            let entity = {
                name: "Pesho",
                age: 22,
                birthday: new Date(1998, 0, 7)}

            repository.add(entity)
            assert.throw(function (){repository.getId(15)},Error,'Entity with id: 15 does not exist!')
            assert.throw(function (){repository.getId(-1)},Error,'Entity with id: -1 does not exist!')
            assert.equal(repository.getId(0).toString(), {"name":"Pesho","age":22,"birthday":"1998-01-06T22:00:00.000Z"})
            repository.add(entity)
            assert.equal(repository.getId(1).toString(), {"name":"Pesho","age":22,"birthday":"1998-01-06T22:00:00.000Z"})
        });
        it("del", function () {
            let repository = new Repository(properties)
            let entity = {
                name: "Pesho",
                age: 22,
                birthday: new Date(1998, 0, 7)}
            repository.add(entity)
            assert.throw(function (){repository.del(15)},'Entity with id: 15 does not exist!')
            assert.throw(function (){repository.del(-1)},'Entity with id: -1 does not exist!')
            assert.throw(function (){repository.del('test')},'Entity with id: test does not exist!')
            assert.equal(function (){
                let size = repository.count
                repository.del(0)
                let newSize = repository.count
                return [size, newSize]
            }().toString(), [1,0])
        });
        it('deletes correctly', () => {
            let repository = new Repository(properties)
            let validEntity = {
                name: "Pesho",
                age: 22,
                birthday: new Date(1998, 0, 7)}
            repository.add(validEntity);
            repository.add(validEntity);

            assert.equal(repository.count,2);
            repository.del(1);
            assert.equal(repository.count,1);
            repository.del(0);
            assert.equal(repository.count,0);
            assert.throw(() => repository.del(0),'Entity with id: 0 does not exist!');
        });
        it("update", function () {
            let repository = new Repository(properties)
            let entity = {
                name: "Pesho",
                age: 22,
                birthday: new Date(1998, 0, 7)}
                repository.add(entity)
            entity = {
                name: 'Gosho',
                age: 22,
                birthday: new Date(1998, 0, 7)
            };
            repository.update(0, entity)
            assert.equal(repository.getId(0).toString(),{"name":"Gosho","age":22,"birthday":"1998-01-06T22:00:00.000Z"})
            assert.equal(repository.count, 1)
            let anotherEntity = {
                name1: 'Stamat',
                age: 29,
                birthday: new Date(1991, 0, 21)
            };

            assert.throw(function (){repository.update(0, anotherEntity)},Error,`Property name is missing from the entity!`)
            anotherEntity = {
                name: 'Stamat',
                age: 29,
                birthday: 1991
            };
            assert.throw(function (){repository.update(0, anotherEntity)},TypeError,`Property birthday is not of correct type!`)
        });
        it("_validate", function () {
            let entity = {
                name1: 'Stamat',
                age: 29,
                birthday: new Date(1991, 0, 21)
            };
            let Entity = {
                name: 'Stamat',
                age: 29,
                birthday: 1991}
            let entityOk = {
                name: "Pesho",
                age: 22,
                birthday: new Date(1998, 0, 7)}

            let repository = new Repository(properties)
            assert.throws(function (){repository._validate(entity)},Error, `Property name is missing from the entity!`)
            assert.equal(repository._validate(entityOk), undefined)
            assert.throws(function (){repository._validate(Entity)},Error, `Property birthday is not of correct type!`)
        });
    });
});
