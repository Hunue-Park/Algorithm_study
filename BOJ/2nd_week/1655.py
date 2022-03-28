# let's say middle number 

import sys
import heapq

input = sys.stdin.readline

N = int(input())

# 중간값보다 작거나 같은 수들을 넣을 힙
l_heap = []
# 중간값보다 큰 수들을 넣는 힙
r_heap = []
answer = []

for i in range(N):
    # 입력 받는 수 
    input_num = int(input())
    # 만약 left 와 right 힙의 개수가 같은 상태에서 넣는 거라면
    # 짝수개에서 홀수개가 되는 것이므로 left 의 루트가 바로 답이 될수있도록 left에 넣는다. (left는 max heap)
    if len(l_heap) == len(r_heap):
        heapq.heappush(l_heap, (-input_num, input_num))
    # 길이가 다른 상태 -> 바로 이전에 left에 먼저 넣을것이기때문에 left가 더 긴상태. 홀수개에서 짝수개로 될것이므로
    # 문제의 규칙상 중간값이 두개라면 작은쪽을 답으로 하기때문에 left 의 루트가 출력값인건 유지된다. 
    else:
        heapq.heappush(r_heap, (input_num, input_num))
    # r_heap 에 값이 존재하고, l_heap의 최대값이 r_heap의 최소값보다 작다면 
    if r_heap and l_heap[0][1] > r_heap[0][1]:
        # 최소값을 r heap의 뽑아낸 루트 값으로 하고 
        # 최대값을 l heap의 뽑아낸 루트값으로해서 다시 뒤바꾼다음 서로에 집어넣는다. 
        min = heapq.heappop(r_heap)[1]
        max = heapq.heappop(l_heap)[1]
        # l heap은 최대힙이기때문에 우선순위에 - 붙여서 집어넣는다. 
        heapq.heappush(l_heap, (-min, min))
        heapq.heappush(r_heap, (max, max))
    # 위 과정을 거치면 결과적으로 l heap의 루트에는 중간값이 남게된다. 
    answer.append(l_heap[0][1])

for j in answer:
    print(j)