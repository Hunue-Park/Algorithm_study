# down side slope
from collections import deque
import sys
input = sys.stdin.readline
rows, cols = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(rows)]
visited = [[0] * cols for _ in range(rows)]
dp = [[0] * cols for _ in range(rows)]

def check_range(r, c):
    return (0 <= r < rows) and (0 <= c < cols)

# 특정 점까지의 내리막길 경로개수의 최대값을 저장해 놓는 dp 테이블
q = deque()
moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
q.append([0, 0])
while q:
    r, c = q.popleft()
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if check_range(nr, nc) and maps[nr][nc] < maps[r][c]:
            if visited[nr][nc] == 1:
                dp[nr][nc] += 1
            visited[nr][nc] = 1
            dp[nr][nc] = max(dp[nr - 1][nc], dp[nr][nc - 1], dp[nr + 1][nc], dp[nr][nc + 1])

print(dp[-1][-1])

