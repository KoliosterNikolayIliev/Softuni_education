from project.software.software import Software


class Hardware:

    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        occupied_memory = sum([x.memory_consumption for x in self.software_components])
        occupied_capacity = sum([x.capacity_consumption for x in self.software_components])
        if software.capacity_consumption + occupied_capacity > self.capacity \
                or software.memory_consumption + occupied_memory > self.memory:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
