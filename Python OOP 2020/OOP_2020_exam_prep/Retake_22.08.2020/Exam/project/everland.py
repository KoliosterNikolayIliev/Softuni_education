from project.appliances.appliance import Appliance
from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([(x.expenses + x.room_cost) for x in self.rooms])
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_expenses = room.expenses + room.room_cost
            if room.budget >= total_expenses:
                result.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.")
                room.budget -= total_expenses
            else:
                name = room.family_name
                self.rooms.remove(room)
                result.append(f"{name} does not have enough budget and must leave the hotel.")
        return "\n".join(result)

    def status(self):
        n = 0
        people = sum([x.members_count for x in self.rooms])
        result = f"Total population: {people}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if room.children:
                for child in room.children:
                    n += 1
                    result += f"--- Child {n} monthly cost: {child.cost:.2f}$\n"
            cost_appliances = 0
            if room.appliances:
                for App in room.appliances:
                    if isinstance(App, Appliance):
                        cost_appliances += App.get_monthly_expense()
                result += f"--- Appliances monthly cost: {cost_appliances:.2f}$\n"

        return result
