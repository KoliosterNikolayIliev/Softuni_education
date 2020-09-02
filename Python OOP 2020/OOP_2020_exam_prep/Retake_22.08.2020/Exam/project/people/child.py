class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.food_cost = food_cost
        self.cost = food_cost
        self.toys = toys_cost
        for i in self.toys:
            self.cost +=i

    def get_monthly_expense(self):
        return self.cost * 30


        #TODO - not sure for toys_cost





