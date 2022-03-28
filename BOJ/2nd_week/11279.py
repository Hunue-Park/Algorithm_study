# max heap
import heapq
import sys

input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    num = int(input())

    if num == 0:
        if heap:
            # heap 에서 가장 큰값 . 최대힙이므로. 
            print(heapq.heappop(heap)[1])
        else:
            print("0")
    else:
        heapq.heappush(heap, [-num, num])

print(heap, "heap")