from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str,
                                  capacity_consumption: int, memory_consumption: int):
        hardware_list = [h for h in System._hardware if h.name == hardware_name]
        if hardware_list:
            hardware = hardware_list[0]
            express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            try:
                hardware.install(express_software)
                System._software.append(express_software)
            except Exception:
                return "Software cannot be installed"
        else:
            return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str,
                                capacity_consumption: int, memory_consumption: int):
        hardware_list = [h for h in System._hardware if h.name == hardware_name]
        if hardware_list:
            hardware = hardware_list[0]
            light_software = LightSoftware(name, capacity_consumption, memory_consumption)
            try:
                hardware.install(light_software)
                System._software.append(light_software)
            except Exception:
                return "Software cannot be installed"
        else:
            return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware_list = [h for h in System._hardware if h.name == hardware_name]
        software_list = [s for s in System._software if s.name == software_name]
        if software_list and hardware_list:
            software = software_list[0]
            hardware = hardware_list[0]
            hardware.uninstall(software)
            # not written in exam
            System._software.remove(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        hardware_components = len(System._hardware)
        software_components = len(System._software)
        total_memory = sum([h.memory for h in System._hardware])
        total_used_memory = sum(
            [software.memory_consumption for h in System._hardware for software in h.software_components])
        total_capacity = sum([h.capacity for h in System._hardware])
        total_used_capacity = sum(
            [software.capacity_consumption for h in System._hardware for software in h.software_components])
        return f"System Analysis\n" \
               f"Hardware Components: {hardware_components}\n" \
               f"Software Components: {software_components}\n" \
               f"Total Operational Memory: {total_used_memory:.0f} / {total_memory:.0f}\n" \
               f"Total Capacity Taken: {total_used_capacity:.0f} / {total_capacity:.0f}"

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n"
            number = len([software for software in hardware.software_components if
                          software.__class__.__name__ == "ExpressSoftware"])
            result += f"Express Software Components: {number}\n"
            number = len([software for software in hardware.software_components if
                          software.__class__.__name__ == "LightSoftware"])
            result += f"Light Software Components: {number}\n"
            used = sum([s.memory_consumption for s in hardware.software_components])
            result += f"Memory Usage: {used:.0f} / {hardware.memory:.0f}\n"
            used = sum([s.capacity_consumption for s in hardware.software_components])
            result += f"Capacity Usage: {used:.0f} / {hardware.capacity:.0f}\n"
            result += f"Type: {hardware.type}\n"
            components = None if not hardware.software_components else ', '.join(
                software.name for software in hardware.software_components)
            result += f"Software Components: {components}"
        return result
