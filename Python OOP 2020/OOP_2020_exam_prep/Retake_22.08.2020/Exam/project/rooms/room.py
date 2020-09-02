class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value=0):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args):
        # TODO - needs to be checked (monthly or daily), and check args
        total_cost = 0
        for el in args:
            cost = [x.get_monthly_expense() for x in el]
            if cost:
                total_cost += sum(cost)
        self.expenses = total_cost
