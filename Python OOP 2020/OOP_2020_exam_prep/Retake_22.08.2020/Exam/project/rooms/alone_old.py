from project.rooms.room import Room


class AloneOld(Room):

    def __init__(self, family_name: str, pension: float):
        Room.__init__(self, family_name, pension, 1)
        self.room_cost = 10
        self.appliances = []
