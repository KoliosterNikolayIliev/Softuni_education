from project.appliances.appliance import Appliance


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    # TODO - smelly class - needs to be checked property expenses
    @property
    def family_name(self):
        return self.__family_name

    @family_name.setter
    def family_name(self, value):
        self.__family_name = value

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @property
    def members_count(self):
        return self.__members_count

    @members_count.setter
    def members_count(self, value):
        self.__members_count = value

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
        cost = []
        for el in args:
            for i in el:
                if isinstance(i, Appliance):
                    cost.append(i.get_monthly_expense())
                else:
                    cost.append(i.cost)
            if cost:
                total_cost += sum(cost)
        self.expenses = total_cost
