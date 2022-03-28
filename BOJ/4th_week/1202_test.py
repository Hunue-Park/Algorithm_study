# jewls theif

import sys
import heapq

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

result = [] 
for bag in bags:
    # 가방 보다 가벼운 애들을 다 후보로서 result 에 보냄
    while jewls and bag >= jewls[0][0]:
        # 맥스힙이기 때문에 가격이 높은 순으로 정렬됨
        heapq.heappush(result, -jewls[0][1])
        heapq.heappop(jewls) 
    # result 에서 꺼낼때 하나씩만 꺼내서 더함. 그러면 어차피 그다음 가방 무게는 
    # 더 많은 걸 담을 수 있으므로 무조건 다음으로 높은 가격의 보석을 담을 수 있음. 
    if result:
        ans += heapq.heappop(result)
    # elif not jewls: 
    #     break


print(-ans)
