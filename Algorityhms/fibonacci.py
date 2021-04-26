from binarytree import Node, build


def fibonacci(n, memo={}):
    if n == 0:
        return n + 1, 0
    if n in memo:
        return n + 1, memo[n]
    if n <= 2:
        return n + 1, 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return n + 1, memo[n]


def run(n):
    sequence = []
    for i in range(n):
        sequence.append(fibonacci(i)[0])
    return sequence


# if __name__ == "__main__":
#     print(run(6))
#     root = build(reversed(run(6)))
#     print(root)
#     # print(run(int(input('Enter number:'))))

def draw_fibonacci_tree(n):
    root = Node(n)
    # left
    root.left = Node(n - 1)
    eval("root.left.left = Node(n - 2)")
    root.left.left.left = Node(n - 3)
    root.left.left.right = Node(n - 4)
    root.left.left.left.left = Node(n - 4)
    root.left.left.left.right = Node(n - 5)
    root.left.right = Node(n - 3)
    root.left.right.left = Node(n - 4)
    root.left.right.right = Node(n - 5)

    # right
    root.right = Node(n - 2)
    root.right.right = Node(n - 4)
    root.right.left = Node(n - 3)
    root.right.left.left = Node(n - 4)
    root.right.left.right = Node(n - 5)
    print(root)


draw_fibonacci_tree(6)
