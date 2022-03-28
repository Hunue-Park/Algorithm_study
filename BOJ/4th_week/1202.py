# juel theif
import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
jewls = []
bags = []
for _ in range(N):
    jewls.append(list(map(int, input().split())))


for _ in range(K):
    bags.append(int(input()))

bags.sort()
jewls.sort()
ans = 0

temp = []
# 가방 무게도 힙에서 꺼낼 필요는 없다. 
for bag in bags:
    while jewls and bag >= jewls[0][0]:
        heapq.heappush(temp, -jewls[0][1])
        heapq.heappop(jewls)
    # temp 에 들어간다는건 조건에 해당한다는 뜻. 
    if temp:
        ans += heapq.heappop(temp)
    elif not jewls:
        break


print(-ans)

