class MyClass:
    def __init__(self, person, name, age):
        self.person = person
        self.name = name
        self.age = age

    def find_age(self, family_name):
        print(f'This person is {self.person} of {self.age} and his name is {family_name}')
        print(type(self.person))


new_person = MyClass('male', 'Pesho', 65)

new_person.find_age('Goshev')


class Pesho(MyClass):
    def __init__(self, person, name, age, drinking):
        super(Pesho, self).__init__(person, name, age)
        self.drinking = drinking

    @property
    def is_drinking(self):
        return self.drinking


gosho = Pesho('Yes', 'Pesho bre', 155, 'For sure')

drinks = gosho.is_drinking
print(drinks)