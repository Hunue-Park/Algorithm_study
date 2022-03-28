# #팀 나누기. 브루트포스, 백트래킹

# 축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 
# 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.

# 입력
# 첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 
# 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

import sys
from itertools import permutations, combinations

N = int(sys.stdin.readline())

abilities = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

orders = [i for i in range(N)]

order_2 = list(combinations(orders, int(N/2)))

# print(list(order_2[1]))

#a_sub_b = [x for x in orders if x not in order_2[i]]

min_gap = 1000000
for i in range(len(order_2) // 2):
    ans_start = 0
    
    start_team = list(order_2[i])
    #link_team = [x for x in orders if x not in order_2[i]]
    
    for j in range(N // 2):
        member = start_team[j]
        for k in start_team:
            ans_start += abilities[member][k]

    link_team = list(order_2[-i-1])
    ans_link = 0
    for j in range(N//2):
        member = link_team[j]
        for k in link_team:
            ans_link += abilities[member][k]
    


    
    
    min_gap = min(abs(ans_start - ans_link), min_gap)
    

print(min_gap)


