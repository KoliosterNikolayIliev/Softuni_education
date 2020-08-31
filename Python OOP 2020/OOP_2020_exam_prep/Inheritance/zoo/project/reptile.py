from project.animal import Animal


class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)

#
# reptile = Reptile("Mosho")
# print(f'The reptile {reptile.name}')