# moving~
from collections import deque
import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())

dp = [[0]* (cols + 1) for _ in range(rows+1)]

candies = [list(map(int, input().split())) for _ in range(rows)]


for i in range(1, rows+1):
    for j in range(1, cols+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + candies[i-1][j-1]

print(dp[-1][-1])
