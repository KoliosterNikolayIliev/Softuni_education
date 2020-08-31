from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name, capacity):
        Factory.__init__(self, name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        ingredient_types = ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]
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

    def add_recipe(self, recipe_name: str, recipe: dict):
        if recipe_name in self.recipes:
            recipe[recipe_name].update(recipe)
        else:
            self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if recipe_name not in self.recipes:
            raise TypeError("No such recipe")

        for prod, qty in self.recipes[recipe_name].items():
            self.remove_ingredient(prod, qty)
            self.capacity += qty
        if recipe_name not in self.products:
            self.products[recipe_name] = 1
        else:
            self.products[recipe_name] += 1
