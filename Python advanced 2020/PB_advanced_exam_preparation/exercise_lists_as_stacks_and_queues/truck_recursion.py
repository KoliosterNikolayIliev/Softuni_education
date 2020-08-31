from collections import deque

n = int(input())
stations = deque()
fuel_left = 0
index = 0
for i in range(n):
    station = [int(x) for x in input().split()]
    stations.append(station)


def solve():
    global stations, fuel_left, index

    cur_station = stations.popleft()
    fuel = cur_station[0]
    distance = cur_station[1]
    fuel_left = fuel_left + fuel - distance
    if fuel_left < 0:
        index += 1
        fuel_left = 0
        stations.append(cur_station)
    if stations:
        solve()
    else:
    return index


print(solve())
