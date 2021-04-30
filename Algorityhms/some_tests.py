# class MyClass:
#     def __init__(self, person, name, age):
#         self.person = person
#         self.name = name
#         self.age = age
#
#     def find_age(self, family_name):
#         print(f'This person is {self.person} of {self.age} and his name is {family_name}')
#         print(type(self.person))
#
#
# new_person = MyClass('male', 'Pesho', 65)
#
# new_person.find_age('Goshev')
#
#
# class Pesho(MyClass):
#     def __init__(self, person, name, age, drinking):
#         super(Pesho, self).__init__(person, name, age)
#         self.drinking = drinking
#
#     @property
#     def is_drinking(self):
#         return self.drinking
#
#
# gosho = Pesho('Yes', 'Pesho bre', 155, 'For sure')
#
# drinks = gosho.is_drinking
# print(drinks)
#
# def fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#
#     elif n == 0:
#         return 0
#
#     elif n == 1 or n == 2:
#         return 1
#
#     else:
#         result = fibonacci(n - 1) + fibonacci(n - 2)
#         return result
#
#
#
# print(fibonacci(5))
# print(fibonacci(6))
# print(fibonacci(7))

"""binary tree inversion"""

# (creating the tree)
import copy


def invert_tree(node):
    if node is None:
        return None
    node.left, node.right = node.right, node.left
    invert_tree(node.left)
    invert_tree(node.right)

    return node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


sample_tree = TreeNode(1)
sample_tree.left = TreeNode(2)
sample_tree.right = TreeNode(3)
sample_tree.left.left = TreeNode(4)
sample_tree.left.right = TreeNode(5)
sample_tree.right.left = TreeNode(6)
sample_tree.right.right = TreeNode(7)


def print_tree(root):
    print(root.val)
    if root.left:
        print_tree(root.left)
    if root.right:
        print_tree(root.right)


print_tree(sample_tree)
inverted_tree = invert_tree(sample_tree)
print_tree(inverted_tree)
