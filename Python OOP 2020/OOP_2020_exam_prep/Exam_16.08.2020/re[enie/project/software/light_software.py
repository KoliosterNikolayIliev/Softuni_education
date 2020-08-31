from project.software.software import Software


class LightSoftware(Software):

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, 'Light', capacity_consumption, memory_consumption)
        self.capacity_consumption = int(1.5 * self.capacity_consumption)
        self.memory_consumption = int(0.5 * self.memory_consumption)
