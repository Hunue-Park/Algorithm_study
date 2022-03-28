#외판원순회 문제!
# 이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다. 
# 단, 한 번 갔던 도시로는 다시 갈 수 없다.
#2차원 리스트 만들기! 
import sys
from itertools import combinations, permutations

def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret



N = int(sys.stdin.readline())

Col = N
Row = N

cost_board = [[0 for i in range(Col)] for j in range(Row)]

for i in range(N):
    cost_board[i] = list(map(int, input().split()))



permuted_nums = []
for i in range(N):
    # i 2 3 4 i 와 같은 방식. 우선 이러한 인덱스 들로 이루어진 리스트를 생성. 
    villages = []
    # for 문 내부에서 생성해서 계속해서 초기화 할 수 잇도록 한다.
    for j in range(N):
        villages.append(j)
    #i 부터 출발해서 i 까지 돌아오는 permutation 생성. 단, i 는 permutation에서 제외해야함.
    villages.remove(i)
    permuted_village = list(permutations(villages))
    
    #외부 리스트, permuted_nums 에 마을 순회조합(i를 제외한)을 집어넣는다. 
    permuted_nums.append(permuted_village)

#permuted_nums = [[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)], 
#                 [(0, 2, 3), (0, 3, 2), (2, 0, 3), (2, 3, 0), (3, 0, 2), (3, 2, 0)], 
#                 [(0, 1, 3), (0, 3, 1), (1, 0, 3), (1, 3, 0), (3, 0, 1), (3, 1, 0)],
#                 [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]]



#변환시킨 조합을 넣을 리스트
#converted_permutes = []

#밑의 for 문 j 가 변하는 범위인 (n-1)! 을 계산해서 변수로 선언해준다.
p = factorial(N-1)

mx = 1000

#튜플로 된 조합을 리스트로 변환 후, 삭제했던 인덱스를 앞뒤로 삽입
for i in range(N):
    for j in range(p):   #j 가 변하는 구간에서 (n-1)! 값이 들어가야한다
        target_permutes = list(permuted_nums[i][j])
        target_permutes.insert(0, i)
        target_permutes.insert(len(target_permutes), i)
        # print(target_permutes)
        # converted_permutes.append(target_permutes)

        total_costs = 0
        for s in range(len(target_permutes)-1):
            k = target_permutes[s]
            l = target_permutes[s+1]
            if cost_board[k][l] == 0:    #이 부분에서 k != l 인 경우에 total_cost를 계산하지 않는 조치가 필요함.
                continue
            elif cost_board[k][l] != 0:
                total_costs = total_costs + cost_board[k][l]
        #경로의 합을 mx 와 비교하여 작으면 mx 로 계속해서 갱신해나간다.
        
        

        if mx > total_costs:
            mx = total_costs
        elif mx <= total_costs:
            mx = mx
        
        
print(mx)