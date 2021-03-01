

# class Mammal:
#     def __init__(self, legs, tail):
#         self.legs = legs
#         self.tail = tail
#
#
# class Cat(Mammal):
#     def __init__(self, legs, tail, claws):
#         super().__init__(legs, tail)
#         self.claws = claws
#
#
# class Dog(Mammal):
#     def __init__(self, legs, tail, brand):
#         Mammal.__init__(self, legs, tail)
#         self.brand = brand
#
#
# new_cat = Cat(4, 1, 16)
# ne_dog = Dog(4, 1, 'Street')
#
# print([new_cat.legs, new_cat.tail, new_cat.claws])
# print([ne_dog.legs, ne_dog.tail, ne_dog.brand])

class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    @staticmethod
    def full_name(a, b):
        return a + b


new_person = Person('tosho', 'peshev')

full_name = new_person.full_name(new_person.name, new_person.lastname)

print (full_name)
