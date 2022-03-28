import sys
import heapq
n = int(sys.stdin.readline().rstrip("\n"))
nums = []
for _ in range(n):
    value, day = map(int, sys.stdin.readline().rstrip().split())
    nums.append([value, day])
nums = sorted(nums, key=lambda x:x[1])
sums = []
for num in nums:
    heapq.heappush(sums,num[0])
    # 여기가 핵심. 리스트의 길이와 강연의 데드라인을 비교. 
    if(len(sums) > num[1]):
        heapq.heappop(sums)
print(sum(sums))