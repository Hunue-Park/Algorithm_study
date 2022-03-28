# jump
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 어차피 1번 부터 N 번 돌까지 이므로 굳이 리스트를 따로 만들지 말고 for 문의 i 를 
# 차례대로 돌리면 됨.

dp = [[float('inf')] * (int((2*N) ** 0.5) + 2) for _ in range(N+1)]
dp[1][0] = 0

small_stones = set()
for _ in range(M):
    small_stones.add(int(input()))
for i in range(2, N + 1):
    if i in small_stones:
        continue
    for j in range(1, int((2 * i ) **0.5) + 1):
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j + 1]) + 1 # + 1 은 점프 횟수의 증가

if min(dp[N]) == float('inf'):
    print(-1)
else:
    print(min(dp[N]))

print(dp)