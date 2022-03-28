# card sorting
# make cards minimum heap sorted and pop it from root 
# append another list and sum 

import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    input_num = int(input())
    heapq.heappush(heap, (input_num, input_num))

n = N

if len(heap) == 1:
    print(0)
else:
    answer = 0
    while len(heap) > 1:
        extract_1 = heapq.heappop(heap)[1]
        extract_2 = heapq.heappop(heap)[1]
        answer += extract_1 + extract_2
        heapq.heappush(heap, (extract_1 + extract_2, extract_1 + extract_2))

    print(answer)

