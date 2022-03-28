# make bigger 

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().strip()))

result = []
del_num = k

for i in range(n):
    # 지우는 횟수가 아직 0보다 크고, 결과리스트에 값이 있는동안 반복
    while del_num > 0 and result:
        # 스택의 마지막 값과 i 번째 넣을 수도 있는 값을 비교 후 더 크다면 
        if result[-1] < nums[i]:
            # 스택에서 마지막 값을 꺼내고 
            result.pop()
            # 꺼냈으니 제거횟수 하나 줄이고
            del_num -= 1
        else:
            break
    result.append(nums[i])
    print(result)

for i in range(n - k):
    print(result[i], end="")
