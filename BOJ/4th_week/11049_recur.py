import sys

input = sys.stdin.readline

N = int(input())
dp = [[0] * N for _ in range(N)]
matrix_info = [list(map(int, input().split())) for _ in range(N)]

for i in range(N - 1):
    dp[i][i + 1] = matrix_info[i][0] * matrix_info[i + 1][0] * matrix_info[i + 1][1]

def get_min_value(start, end):
    if dp[start][end] != 0:
        return dp[start][end]
    if start == end:
        return 0

    min_value = 2 ** 31
    for k in range(start, end):
        min_value = min(
            min_value,
            get_min_value(start, k) + get_min_value(k + 1, end) + matrix_info[start][0] * matrix_info[k + 1][0] * matrix_info[end][1]
        )
    dp[start][end] = min_value

    return min_value

print(get_min_value(0, N - 1))