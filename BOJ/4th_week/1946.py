# newbiess

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cnt = 1
    people = []
    N = int(input())
    for _ in range(N):
        paper, interview = map(int, input().split())
        people.append([paper, interview])
    
    people.sort(key= lambda x: x[1])
    Max = people[0][0]
    for i in range(1, N):
        if Max > people[i][0]:
            cnt += 1
            Max = people[i][0]
    
    print(cnt)