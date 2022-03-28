# stickers with DP

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    if M == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    dp[0][1] = dp[1][0] + dp[0][1]
    dp[1][1] = dp[0][0] + dp[1][1]
    for j in range(2, M):
        dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + dp[0][j]
        dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + dp[1][j]

    result = max(dp[0][M-1], dp[1][M-1])
    print(result)