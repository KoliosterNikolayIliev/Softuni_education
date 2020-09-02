from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        Room.__init__(self, family_name, salary_one + salary_two, 2 + len(children))
        self.room_cost = 30
        for child in children:
            self.children.append(child)
        self.appliance = [TV(), Fridge(), Laptop()]
        self.appliances = []
        for i in range(self.members_count):
            self.appliances.extend(self.appliance)
        self.costs = []
        self.costs.extend(self.children)
        self.costs.extend(self.appliances)
        self.calculate_expenses(self.costs)
