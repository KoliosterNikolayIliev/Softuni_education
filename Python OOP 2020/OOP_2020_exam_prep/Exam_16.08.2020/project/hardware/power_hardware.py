from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        Hardware.__init__(self, name, "Power", capacity, memory)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        value *= 0.25
        self.__capacity = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        value *= 1.75
        self.__memory = value
