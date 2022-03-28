# 구명보트 with knapsack algorithm
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값.
# n <= 50,000
from collections import deque
people = [70, 50, 80, 50]

limit = 100

people.sort()

people_line = deque()

for i in range(len(people)):
    people_line.append(people[i])

person_weight = 0
boat_count = 0
while people_line:
    if len(people_line) >= 2:
        if people_line[0] + people_line[-1] <= limit:
            people_line.pop()
            people_line.popleft()
            boat_count += 1
        elif people_line[0] + people_line[-1] > limit:
            people_line.pop()
            boat_count += 1
    else:
        if people_line[0] <= limit:
            people_line.pop()
            boat_count += 1

print(boat_count)