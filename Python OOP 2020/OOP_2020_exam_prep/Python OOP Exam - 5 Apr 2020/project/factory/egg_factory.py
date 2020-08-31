from project.factory.factory import Factory


class EggFactory(Factory):
    def __init__(self, name, capacity):
        Factory.__init__(self, name, capacity)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        ingredient_types = ["chicken egg", "quail egg"]
        if ingredient_type not in ingredient_types:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        if ingredient_type in self.ingredients:
            self.ingredients[ingredient_type] += quantity
        else:
            self.ingredients[ingredient_type] = quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients:
            raise KeyError("No such product in the factory")
        if self.ingredients[ingredient_type] < quantity:
            raise ValueError("Ingredient quantity cannot be less than zero")
        self.ingredients[ingredient_type] -= quantity

    @property
    def products(self):
        return self.ingredients
