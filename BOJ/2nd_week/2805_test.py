import sys
input = sys.stdin.readline


def binary_search(low, high):
    global answer
    if low > high:
        return 
    mid = (low + high) // 2

    wood = 0
    for tree in woods:
        if tree > mid:
            wood += tree - mid
    if wood >= M:
        answer = mid
        binary_search(mid+1, high)
    else:
        binary_search(low, mid-1)


N, M = map(int, input().split())

woods = sorted(list(map(int, input().split())))
answer = 0

binary_search(0, max(woods))

print(answer)

# 벌목 높이를 0 부터 최대 나무 높이까지 설정한 다음 이분탐색 진행. 

