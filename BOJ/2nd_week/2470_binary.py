## two liquid binary solution

import sys

N = int(sys.stdin.readline())
liquids = sorted(list(map(int, sys.stdin.readline().split())))

start = 0
end = len(liquids) - 1

# 이건 최소값 갱신 알고리즘을 위한 '암거나 넣는 졸라 큰수' 의 역할
min = sys.maxsize

while start < end:
    calc = liquids[start] + liquids[end]
    if abs(calc) < min:
        min = abs(calc)
        ans = [liquids[start], liquids[end]]  
    if calc == 0:
        break
    if calc < 0:
        start += 1
    else:
        end -= 1

print(ans[0], ans[1])


### 이게 가장 깔끔하다. #####
##### 이분탐색이라기 보다는 start 와 end 가 각각 움직이기 때문에 투포인터네 ######