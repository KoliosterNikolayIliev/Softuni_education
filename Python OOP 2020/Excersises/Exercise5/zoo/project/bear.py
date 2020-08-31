from project.mammal import Mammal


class Bear(Mammal):
    def __init__(self, name):
        Mammal.__init__(self, name)


# bear = Bear("Sasho")
# print(f'bear {bear.name}')
