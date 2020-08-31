from Polymorphism_magic_methods.project.groups import Group
from Polymorphism_magic_methods.project.groups import Person

import unittest


class PersonTest(unittest.TestCase):
    def setUp(self):
        self.person1 = Person("Pesho", "Goshev")

    def test_custom_add(self):
        person2 = Person("Tosho", "Mosho")
        person3 = self.person1 + person2
        self.assertEqual(person3.name, "Pesho")
        self.assertEqual(person3.surname, "Mosho")

    def test_str__Returns_name_surname(self):
        result = f"{self.person1.name} {self.person1.surname}"
        self.assertEqual(result, f"Pesho Goshev")



class GroupTest(unittest.TestCase):
    def setUp(self):
        self.per1 = Person("Gunio", "Prostia")
        self.per2 = Person("Emir", "Kusturica")
        self.group = Group("test_group", [self.per1, self.per2])

    def test_custom_len_returns_count_of_people(self):
        result = len(self.group.people)
        self.assertEqual(result, 2)

    def test_custom_str_returns_group_name_and_members(self):
        result = str(self.group)
        self.assertIn("Group", result)
        self.assertIn("Gunio", result)
        self.assertIn("Emir", result)
        self.assertNotIn("Jore", result)
        self.assertEqual(result, f"Group test_group with members Gunio Prostia, Emir Kusturica")

    def test_custom_repr_returns_group_name_and_members(self):
        result = repr(self.group)
        self.assertIn("Group", result)
        self.assertIn("Gunio", result)
        self.assertIn("Emir", result)
        self.assertNotIn("Jore", result)
        self.assertEqual(result, f"Group test_group with members Gunio Prostia, Emir Kusturica")

    def test_custom_add_concatenates_two_groups(self):
        person3 = Person("Jore", "Gazo")
        group2 = Group("test_group2", [person3])
        group3 = self.group+group2
        self.assertEqual(len(group3),3)

    def test_custom_getitem_return_indexed_people(self):
        result = self.group[1]
        self.assertEqual(result, f"Person 1: Emir Kusturica")

    def test_custom_getitem_invalid_index(self):
        with self.assertRaises(IndexError):
            result = self.group[2]

    def test_set_attributes(self):
        self.assertEqual(self.group.name, "test_group")
        self.assertEqual(len(self.group.people), 2)


if __name__ == "__main__":
    unittest.main()
