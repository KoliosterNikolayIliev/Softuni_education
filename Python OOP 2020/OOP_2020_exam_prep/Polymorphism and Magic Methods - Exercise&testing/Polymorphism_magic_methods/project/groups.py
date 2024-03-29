class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(name=self.name, surname=other.surname)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __str__(self):
        result = [" ".join((x.name, x.surname)) for x in self.people]
        return f"Group {self.name} with members {', '.join(result)}"

    def __repr__(self):
        result = [" ".join((x.name, x.surname)) for x in self.people]
        return f"Group {self.name} with members {', '.join(result)}"

    def __add__(self, other):
        group = Group(name=f"{self.name}", people=self.people + other.people)
        return group

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index].name} {self.people[index].surname}"



# p0 = Person('Aliko', 'Dangote')
# p1 = Person('Bill', 'Gates')
# p2 = Person('Warren', 'Buffet')
# p3 = Person('Elon', 'Musk')
# p4 = p2 + p3
#
# first_group = Group('__VIP__', [p0, p1, p2])
# second_group = Group('Special', [p3, p4])
# third_group = first_group + second_group
#
# print(len(first_group))
# print(len(second_group))
# print(len(third_group))
#
# print(first_group)
# print(second_group)
# print(third_group)
# print(third_group[0])
# print(second_group[0])
# print(first_group[1])
#
# for person in third_group:
#     print(person)
#
# for person in first_group:
#     print(person)
#
# for person in second_group:
#     print(person)
