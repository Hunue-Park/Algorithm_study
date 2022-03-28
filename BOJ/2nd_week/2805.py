# 이분 탐색의 핵심은 전체 배열을 반씩 쪼개며 탐색해나간다는 점. 
# 주어진 나무높이 배열을 반씩 쪼개며 탐색하는게 아니라 
# 최소 나무 높이 부터 최대 나무 높이까지 자연수로 이루어진 배열을 반씩 쪼개며 탐색해 나가는 건 어떨까
# 핵심구현:
#   1. 절단기 높이 배열에 따른 가져가는 나무 길이와 주어진 목표 나무길이(M) 과의 비교 
#   2. 절단기 높이 선택을 이분탐색으로 
#       2-1. 높이 선택의 이분탐색. 탐색은 내가 원하는 특정 값을 일치하는 값을 리스트에서 찾는과정.
#           일치하는 => 1번 과정의 결과값이 True 인가. 
#            좀 더 자세히: 절단기 높이 값에 따른 '가져가는 나무 길이' == '목표 나무 길이' 이면 해당 절단기 높이값이 답.
# 그런데, "적어도 목표 나무길이"는 {가져가는 나무길이 by 직전절단기높이 > 목표나무길이 
#                       and 가져가는 나무길이 by 현재 절단기 높이 < 목표나무 길이} 라면 현재 절단기 높이가 답
#                       '직전 절단기 높이' < 목표 나무 길이 and 현재 절단기 높이 > 목표 나무 길이 라면 현재 절단기 높이가 답. 
#                    어디서 변화하는가? 를 찾아내야함.  
#   3. 그렇다면 1번 과정에서의 비교 결과값이 boolean 으로 주어져야 할것 같다. 


import sys

N, M = map(int, sys.stdin.readline().split())

Trees = sorted(list(map(int, sys.stdin.readline().split())))

possible_height = [i for i in range(1, Trees[-1])]
#### 이 possible_height 가 쓸데없는 메모리를 너무 많이 잡아먹었으. ###### 
### => 이렇게 푸는 거아님. ######


#core function 1. 절단기 높이 배열에 따른 가져가는 나무 길이와 주어진 목표 나무길이(M) 과의 비교 
def core_1(k):
    tree_sum = 0
    for i in range(N):
        if Trees[i] >= k:
            tree_sum = tree_sum + (Trees[i] - k)
    
    if tree_sum == M:
        return 1
    elif tree_sum > M:  #절단기 높이가 더 커야 한다는 의미 
        return 2
    elif tree_sum < M:  #절단기 높이가 더 낮아야한다는 의미
        return 3
    return 0

#core function 2. 절단기 높이 선택을 이분탐색으로 
#기존 이분탐색 함수에서 타겟을 없애야함. 타겟을 주고 리스트에서 찾는게 아니기 때문.
#array 에는 possible_height 가 들어갈 예정.
# start 와 end 나누는 방향 결정을 어떤 부분에서 해야하나 고민. 
def binary_search(array, start, end):
    if start > end:
        print(0)
        return None
    mid = (start + end) // 2
    k = array[mid]
    # k가 의미하는 바는 possible_height 의 특정 값.
    if core_1(k) == 1 or (core_1(k+1) == 3 and core_1(k) == 2):
        # 변화를 체크하는 방법은 확인했는데 그 변화의 방향에 따라 체크 방법도 조금 바뀌어야할 필요. 
        print(k)
        return
    # 변화의 방향에 따라 k-1 혹은 k 를 출력하는 방식으로 해결. 
    elif (core_1(k-1) == 2 and core_1(k) == 3):
        print(k-1)
        return
    elif core_1(k) == 3:   #절단기 높이가 더 낮아야한다는 의미, 더 왼쪽 배열구간에 타겟 존재한다. 
        return binary_search(array, start, mid - 1)
    elif core_1(k) == 2:  #절단기 높이가 더 커야 한다는 의미, 더 오른쪽 배열구간에 타겟 존재한다
        return binary_search(array, mid + 1, end)

binary_search(possible_height, 0, len(possible_height) - 1)

##### example 까지는 나오는데 어디서 틀린걸까 아마도 tree_sum 이 M 과 같진 않지만 '적어도'를 만족하는 경우 일 것이다. 
## 변화량, 변화의 기점 체크하는 방법 생각. 
## 반례: 3 3, 10 10 12 => 통과. 
### another 반례 : 3 6 , 10 10 12

###### 메모리 초과...@ 쓸데없는 리스트를 잡았다. possible height #####
## 컴퓨터는 한쪽 방향 필터만 걸어놓으면 어차피 이분탐색이기때문에 지가 왔다갔다하면서 답에 가까워지게 되있다. 
## 사람처럼 생각하지 말고 컴퓨터처럼 생각할것. ###



