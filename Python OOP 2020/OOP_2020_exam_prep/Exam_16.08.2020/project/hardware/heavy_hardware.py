from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        Hardware.__init__(self, name, "Heavy", capacity, memory)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        value *= 2
        self.__capacity = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        value *= 0.75
        self.__memory = value
