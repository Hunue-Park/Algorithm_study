#외판원 2트

import sys
from itertools import permutations

N = int(sys.stdin.readline())

villages = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

travel_order = [i for i in range(N)]

def calculating(List):
    ans = 0
    for i in range(N-1):
        if villages[List[i]][List[i+1]] != 0:
            ans += villages[List[i]][List[i+1]]
        else:
            return False
    if villages[List[-1]][List[0]] == 0:
        return False
    else:
        ans += villages[List[-1]][List[0]]
    return ans

ans = 999990999
for List in permutations(travel_order):
    result = calculating(List)
    if result != False:
        if ans > result:
            ans = result

print(ans)
