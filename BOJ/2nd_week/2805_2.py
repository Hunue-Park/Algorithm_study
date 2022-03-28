# 상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 
# 이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. 
# (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

# 둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 
# 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

# 출력
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

import sys

N, M = map(int, sys.stdin.readline().split())

Trees = sorted(list(map(int, sys.stdin.readline().split())))

#mid_value 를 정하는 매커니즘의 구현. 
# Trees리스트의 처음값과 끝값의 중간으로 시작. 이후에 이 값으로 구한 집으로 가져가는 나무의 합(K)이 M 값보다 클 경우 
# 늘려야 하므로 끝값을 더한 평균으로 다시 갱신. 줄여야 한다면 처음값을 더한 평균으로 갱신. 
#initial mid_value
mid_value = (Trees[0] + Trees[-1]) // 2

mids = [mid_value]

def getTreesum(mid_value):
    tree_sum = 0
    for i in range(N):
        if Trees[i] >= mid_value:
            tree_sum = tree_sum + (Trees[i] - mid_value)
    return tree_sum

while mid_value <= Trees[-2] or mid_value >= Trees[1]:
    getTreesum(mid_value)

    if getTreesum(mid_value) > M:
        if getTreesum(mids[-1]) < M:
            print(mid_value)
            break
        mid_value = (mid_value + Trees[-1]) // 2
        print(mid_value)
        mids.append(mid_value)
        #이렇게 구한 mid_value로 다시 for 문 통과
        
    elif getTreesum(mid_value) == M:
        #만약 M과 같아진다면 해당 mid_value가 문제에서 구하고자하는 '절단기의 최대높이'이다. 
        print(mid_value)
        break
    elif getTreesum(mid_value) < M:
        if getTreesum(mids[-1]) > M:
            print(mid_value)
            break
        mid_value = (mid_value + Trees[0]) // 2
        print(mid_value)
        mids.append(mid_value)
        # 다시 midvalue 갱신 과정을 거친다. 
        
############### 중간값을 구하는 방식은 치명적인 단점이 있음. 재귀 종료조건이나 while문의 무한루프를 빠져나올수가 없음 ###################
##### 위 코드의 문제점은 22에서 출발해서 34 40을 거쳐 다시 22(처음값)로 돌아와버리면 무한 루프에 빠진다는 점. ###########

# 이분 탐색의 핵심은 전체 배열을 반씩 쪼개며 탐색해나간다는 점. 
# 주어진 나무높이 배열을 반씩 쪼개며 탐색하는게 아니라 
# 최소 나무 높이 부터 최대 나무 높이까지 자연수로 이루어진 배열을 반씩 쪼개며 탐색해 나가는 건 어떨까
# 핵심구현:
#   1. 절단기 높이 배열에 따른 가져가는 나무 길이와 주어진 목표 나무길이(M) 과의 비교 
#   2. 절단기 높이 선택을 이분탐색으로 
#   3. 그렇다면 1번 과정에서의 비교 결과값이 boolean 으로 주어져야 할것 같다. 


