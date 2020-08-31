from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        Software.__init__(self, name, "Express", capacity_consumption, memory_consumption)

    @property
    def memory_consumption(self):
        return self.__memory_consumption

    @memory_consumption.setter
    def memory_consumption(self, value):
        value *= 2
        self.__memory_consumption = value

