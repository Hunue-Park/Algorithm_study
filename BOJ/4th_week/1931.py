# commition room check in
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
meeting_times = []
for _ in range(N):
    meeting_times.append(list(map(int, input().split())))
meeting_times.sort(key=lambda x: (x[1], x[0]))
# 예제는 끝나는 시간을 기준으로 오름차순 정렬되어있긴함. 고려해야 될 사항 
cnt = 1
idx = 0
q = deque()
q.append(idx)
while q:
    start_idx = q.popleft()
    for i in range(start_idx+1, N):
        if meeting_times[start_idx][1] <= meeting_times[i][0]:
            cnt += 1
            q.append(i)
            break

print(cnt)