from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        Software.__init__(self, name, "Light", capacity_consumption, memory_consumption)

    @property
    def capacity_consumption(self):
        return self.__capacity_consumption

    @capacity_consumption.setter
    def capacity_consumption(self, value):
        value *= 1.5
        self.__capacity_consumption = value

    @property
    def memory_consumption(self):
        return self.__memory_consumption

    @memory_consumption.setter
    def memory_consumption(self, value):
        value *= 0.5
        self.__memory_consumption = value



