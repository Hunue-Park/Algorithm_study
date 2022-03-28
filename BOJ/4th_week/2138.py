# bulb and switch

import sys
input = sys.stdin.readline

def two_flip(i, j, bulbs):
    bulbs[i] = 1 - bulbs[i]
    bulbs[j] = 1 - bulbs[j]


def three_flip(i, bulbs):
    bulbs[i-1] = 1 - bulbs[i-1]
    bulbs[i] = 1 - bulbs[i]
    bulbs[i+1] = 1 - bulbs[i+1]


if __name__ == "__main__":
    N = int(input())

    origins = list(map(int, input().strip()))
    copy = [0] * N
    goals = list(map(int, input().strip()))
    # case seperating 
    for i in range(N):
        copy[i] = origins[i]

    for i in range(2):
        A = origins if i == 0 else copy

        cnt = 0
        for j in range(N):
            if j == 0:
                if i == 0 and A != goals:
                    cnt += 1
                    two_flip(j, j+1, A)

            elif 1 <= j <= N-2:
                if A[j-1] != goals[j-1]:
                    cnt += 1
                    three_flip(j, A)

            elif j == N-1:
                if A[j-1] != goals[j-1]:
                    cnt += 1
                    two_flip(j-1, j, A)

        if A == goals:
            print(cnt)
            break

    if A != goals:
        print(-1)

# 가능한 오류 지점. origin과 copy 를 둘다 진행하는데 따로 break 없음. 