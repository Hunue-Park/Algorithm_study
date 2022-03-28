# # 부분 수열의 합

# N개의 정수로 이루어진 수열이 있을 때, 
# 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 
# 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

# 출력
# 첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

import sys
N, S = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

def dfs(idx, sum):
    global cnt
    #재귀함수 종료조건 
    if idx >= N:
        return
    #sum 값에 인덱스 해당 값을 더해주며 갱신
    sum += nums[idx]
    #그렇게 만들어진 sum 값이 S 값과 같은지 체크
    if sum == S:
        cnt += 1
    # 같지 않다면 이후 재귀로 넘어감. nums 리스트의 인덱스 증가를 통해
    dfs(idx + 1, sum - nums[idx])
    # sum 에 자신을 포함한 경우와 아닌 경우로 나눠서 재귀 접근
    dfs(idx + 1, sum)

cnt = 0
dfs(0, 0)
print(cnt)


