from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_p_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_p_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_h_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_h_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [x for x in System._hardware if x.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        hardware = hardware[0]
        new_e_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(new_e_software)
            System._software.append(new_e_software)

        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [x for x in System._hardware if x.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        hardware = hardware[0]
        new_l_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(new_l_software)
            System._software.append(new_l_software)

        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = [x for x in System._hardware if x.name == hardware_name]
        software = [x for x in System._software if x.name == software_name]
        if len(hardware) != 1 and len(software) != 1:
            return "Some of the components do not exist"
        hardware = hardware[0]
        software = software[0]
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        hardware_components = len(System._hardware)
        software_components = len(System._software)
        total_memory = int(sum([x.memory for x in System._hardware]))
        total_memory_used = int(sum([x.memory_consumption for x in System._software]))
        total_capacity = int(sum([x.capacity for x in System._hardware]))
        total_capacity_used = int(sum([x.capacity_consumption for x in System._software]))
        result = f"System Analysis\nHardware Components: {hardware_components}\n" \
                 f"Software Components: {software_components}\n" \
                 f"Total Operational Memory: {total_memory_used} / {total_memory}\n" \
                 f"Total Capacity Taken: {total_capacity_used} / {total_capacity}"
        return result


    @staticmethod
    def system_split():


        result = ""
        for h in System._hardware:
            component = h.name
            type = h.type
            ll_sw_comp = h.software_components
            ex_sw_comp = len([x for x in ll_sw_comp if x.type == "Express"])
            l_sw_comp = len([x for x in ll_sw_comp if x.type == "Light"])
            total_memory = int(h.memory)
            total_memory_used = int(sum([x.memory_consumption for x in h.software_components]))
            total_capacity = int(h.capacity)
            total_capacity_used = int(sum([x.capacity_consumption for x in h.software_components]))
            if len(ll_sw_comp) > 0:
                ll = f"{', '.join([x.name for x in ll_sw_comp])}"
            else:
                ll = "None"

            result += f"Hardware Component - {component}\nExpress Software Components: {ex_sw_comp}\n" \
                      f"Light Software Components: {l_sw_comp}\n" \
                      f"Memory Usage: {total_memory_used} / {total_memory}\n" \
                      f"Capacity Usage: {total_capacity_used} / {total_capacity}\n" \
                      f"Type: {type}\n" \
                      f"Software Components: {ll}\n"
        return result


