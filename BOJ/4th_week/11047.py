# greedy, coin 0 

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))

for i in range(N-1, -1, -1):
    if K < coins[i]:
        continue
    elif K >= coins[i]:
        idx = i
        break
cnt = 0
while K != 0:
    cnt += K // coins[idx]
    K = K % coins[idx]
    idx -= 1
print(cnt)