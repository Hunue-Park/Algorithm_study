# pelindrom

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

M = int(input())
dp = [[0]* N for _ in range(N)]

# dp 채워넣기

for len_of_num in range(N):
    for start in range(N - len_of_num):
        end = start + len_of_num
        # 개수가 한개인 숫자열은 무조건 펠린드롬
        if start == end:
            dp[start][end] = 1
        # 양옆이 같을때
        elif nums[start] == nums[end]:
            # 두글자로 이루어져있으면
            if start + 1 == end:
                # 무조건 펠린드롬
                dp[start][end] = 1
            # 안쪽 숫자열이 펠린드롬이면 해당 숫자열도 펠린드롬
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1
    
for question in range(M):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])


