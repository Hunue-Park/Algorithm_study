# missing brakets 
# 연산자가 +. - 밖에 없으므로 + 앞뒤로 있는 숫자를 감싸는게 
# 무조건 최소값으로 가는 방법

import sys
input = sys.stdin.readline

equations = input().split('-')
nums = []
for elements in equations:
    cnt = 0
    # 이 split 함수는 리스트 타입으로 반환한다. 
    sub = elements.split('+')
    for sub_elemets in sub:
        cnt += int(sub_elemets)
    nums.append(cnt)
n = nums[0]
for i in range(1, len(nums)):
    n -= nums[i]

print(n)