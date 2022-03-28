# jump jump 

import sys

input = sys.stdin.readline

N = int(input())
jumps = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = 1
if N == 1:
    print(0)
else:
    for i in range(N):
        for j in range(jumps[i] + 1):
            # jump 시 N 밖에 나가면 안되고, jump값이 0이어도 안됨
            # 또한 dp[i] = 0 이면 도달할 수 없는 점이라는 의미이므로 도달 할 수 없는 점에서 
            # 점프는 물론 할 수 없다. 
            if i + j < N and i + j != i and dp[i] != 0:
                if dp[i + j] == 0:
                    dp[i + j] = dp[i] + 1
                else:
                    dp[i + j] = min(dp[i] + 1, dp[i + j])
    if dp[N - 1] == 0:
        print(-1)
    else:
        # 마지막에 -1 을 해주는 이유는 dp[0] = 1 로 시작했기 때문. 
        # 그렇다면 왜 dp[0] 를 1로 시작했는가? 
        # 위에서 dp[i]=0 인 지점에선 점프를 할 수 없으므로.
        print(dp[N - 1] - 1)