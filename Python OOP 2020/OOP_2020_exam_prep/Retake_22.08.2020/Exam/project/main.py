from everland import Everland
from people.child import Child
from rooms.young_couple import YoungCouple
from rooms.young_couple_with_children import YoungCoupleWithChildren

from project.rooms.alone_old import AloneOld
from project.rooms.old_couple import OldCouple

everland = Everland()

def test_one():
    young_couple = YoungCouple("Johnsons", 150, 205)
    alone_old = AloneOld("Smith", 40)
    old_couple = OldCouple("fins", 1000, 65)

    child_one = Child(5, 1, 2, 1)
    child_two = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child_one, child_two)

    everland.add_room(young_couple)
    everland.add_room(young_couple_with_children)
    everland.add_room(alone_old)
    everland.add_room(old_couple)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()