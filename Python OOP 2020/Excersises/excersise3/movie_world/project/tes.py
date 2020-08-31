# class Animal:
#     def eat(self):
#         return "eating..."
#
#
# class Dog(Animal):
#     def bark(self):
#         return "barking..."
#
# dog = Dog()
#
# print(dog.eat())
#
# print(dog.bark())

class Father:
    def __init__(self):
        self.father_name = 'Taylor Evans'


class Mother:
    def __init__(self):
        self.mother_name = 'Bet Williams'


class Daughter(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def get_parent_info(self):
        return f'Father: {self.father_name},Mother: {self.mother_name}'


child = Daughter()
print(child.get_parent_info())
