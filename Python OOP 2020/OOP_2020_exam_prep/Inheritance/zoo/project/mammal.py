from project.animal import Animal


class Mammal(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)


# mamal = Mammal("Gosho")
# print(f'The mammal {mamal.name}')
