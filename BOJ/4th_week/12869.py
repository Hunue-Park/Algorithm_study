# mutals 
import itertools
import sys
input = sys.stdin.readline

N = int(input())
scv = list(map(int, input().split()))

dp = [[[-1] * 61 for _ in range(61)] for _ in range(61)]

def go(a,b,c):
    # 0보다 작은 값이 들어오면 0으로 바꿔서 리턴
    if a < 0:
        return go(0, b, c)
    elif b < 0:
        return go(a, 0, c)
    elif c < 0:
        return go(a, b, 0)
    if a == 0 and b == 0 and c == 0:
        return 0
    elif dp[a][b][c] != -1:
        return dp[a][b][c]
    dp[a][b][c] = 99999999
    for case in list(itertools.permutations([1, 3, 9])):
        # 이렇게 DFS 로 찍고 값을 저장해서 돌아오기때문에 시간초과가 나지 않는다. 
        # 각 permutation 6가지를 매번 돌고오지만 값이 저장되있는 항목은 따로 연산을 수행하지 않음
        dp[a][b][c] = min(dp[a][b][c], go(a - case[0], b - case[1], c - case[2]))
    dp[a][b][c] += 1
    return dp[a][b][c]

scv_unit = [0, 0, 0]
# scv 가 3개 이하인 경우를 위함.
# go 함수는 무조건 인자를 3개 받기때문
for i in range(len(scv)):
    scv_unit[i] = scv[i]

go(scv_unit[0], scv_unit[1], scv_unit[2])
print(dp)