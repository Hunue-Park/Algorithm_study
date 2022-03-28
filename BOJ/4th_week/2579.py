# steps

import sys
input = sys.stdin.readline

N = int(input())
steps = []
for _ in range(N):
    steps.append(int(input()))

dp = [0] * N


if N == 1:
    print(steps[-1])
elif N == 2:
    print(sum(steps))
else:
    dp[0] = steps[0]
    dp[1] = steps[0] + steps[1]
    dp[2] = max(steps[2] + steps[1], steps[2]+steps[0])

    for i in range(3, N):
        dp[i] = max(dp[i-3] + steps[i-1] + steps[i], dp[i-2] + steps[i])

    print(dp[-1])