from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    hardware = []
    software = []

    # def __init__(self):
    #     self._hardware = []
    #     self._software = []
    #
    # @property
    # def hardware(self):
    #     return self._hardware
    #
    # @property
    # def software(self):
    #     return self._software

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System.hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System.hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int):
        hardware = [x for x in System.hardware if x.name == hardware_name]
        if len(hardware) != 1:
            return "Hardware does not exist"
        express = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware[0].install(express)
            System.software.append(express)
        except ValueError as ex:
            return ex

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int):
        hardware = [x for x in System.hardware if x.name == hardware_name]
        if len(hardware) != 1:
            return "Hardware does not exist"
        light = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware[0].install(light)
            System.software.append(light)
        except ValueError as ex:
            return ex

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = [x for x in System.hardware if x.name == hardware_name]
        software = [x for x in System.software if x.name == software_name]
        if len(hardware) == 1 and len(software) == 1:
            hardware[0].uninstall(software[0])
            System.software.remove(software[0])
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_used_memory = sum([x.memory_consumption for x in System.software])
        total_memory = sum([x.memory for x in System.hardware])
        total_used_space = sum([x.capacity_consumption for x in System.software])
        total_capacity = sum([x.capacity for x in System.hardware])
        result = f"System Analysis\nHardware Components: {len(System.hardware)}\nSoftware Components: {len(System.software)}\nTotal Operational Memory: {total_used_memory} / {total_memory}\nTotal Capacity Taken: {total_used_space} / {total_capacity}"
        return result
    @staticmethod
    def system_split():
        hardware_components = [x for x in System.hardware]
        Express_Software_Components = [x.type for x in System.software if x.type == "Express"]
        Light_Software_Components = [x.type for x in System.software if x.type == "Light"]
        total_used_memory = sum([x.memory_consumption for x in System.software])
        total_memory = sum([x.memory for x in System.hardware])
        total_used_space = sum([x.capacity_consumption for x in System.software])
        total_capacity = sum([x.capacity for x in System.hardware])
        Software_Components = [x.name for x in System.software]
        if len(Software_Components)>0:
            ll = f"{', '.join(Software_Components)}"
        else:
            ll = None

        result = ""
        for comp in hardware_components:
            result+=f"Hardware Component - {comp.name}\nExpress Software Components: {len(Express_Software_Components)}\nLight Software Components: {len(Light_Software_Components)}\nMemory Usage: {total_used_memory} / {total_memory}\nCapacity Usage: {total_used_space} / {total_capacity}\nType: {comp.type}\nSoftware Components: {ll}\n"
        return result
