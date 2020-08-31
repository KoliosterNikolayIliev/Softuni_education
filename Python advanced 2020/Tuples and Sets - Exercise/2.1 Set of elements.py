tokens = list(map(int,input().split()))
n_lenght = tokens[0]
m_lenght = tokens[1]

n = set()
m = set()

for _ in range(n_lenght):
    number = int(input())
    n.add(number)

for _ in range(m_lenght):
    number = int(input())
    m.add(number)

intersection = n.intersection(m)

for number in intersection:
    print(number)