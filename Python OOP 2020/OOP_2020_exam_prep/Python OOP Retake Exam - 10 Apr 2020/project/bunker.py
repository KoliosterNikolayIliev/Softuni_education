from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food = [x for x in self.supplies if x.__class__.__name__ == "FoodSupply"]
        if not food:
            raise IndexError("There are no food supplies left!")
        return food

    @property
    def water(self):
        water = [x for x in self.supplies if isinstance(x, WaterSupply)]
        if not water:
            raise IndexError("There are no water supplies left!")
        return water

    @property
    def painkillers(self):
        painkillers = [x for x in self.medicine if x.__class__.__name__ == "Painkiller"]
        if not painkillers:
            raise IndexError("There are no painkillers left!")
        return painkillers

    @property
    def salves(self):
        salves = [x for x in self.medicine if x.__class__.__name__ == "Salve"]
        if not salves:
            raise IndexError("There are no salves left!")
        return salves

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            med = self.medicine.pop()
            med.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            sup = self.supplies.pop()
            sup.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")
