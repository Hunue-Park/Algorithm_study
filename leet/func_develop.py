# programmers. stack & queue

from collections import deque
from typing import Tuple

q = deque()

progresses = [95, 90, 99, 99, 80, 99]

speeds = [1, 1, 1, 1, 1, 1]

for i in range(len(progresses)):
    q.append(progresses[i])
#q[0] = [93, 30, 55]

global day
day = 0
def counting_days(q, day):
    for i in range(len(q)):
        q[i] += speeds[i]
    day += 1
    return day

def pick_up_100(q, checknum):
    while q:
        picked = q.popleft()
        if picked >= 100:
            checknum += 1
            continue
        else:
            q.appendleft(picked)
            break
    return checknum
    
release_list = []
while q:
    counting_days(q, day)
    releases = pick_up_100(q, checknum=0)
    release_list.append(releases)

answer = []
for num in release_list:
    if num != 0:
        answer.append(num)
    else:
        continue

print(answer)
    
    



