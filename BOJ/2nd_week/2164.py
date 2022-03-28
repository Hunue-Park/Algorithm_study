# card 2
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
que = deque([i for i in range(1, N+1)])

while len(que) > 1:
    que.popleft()
    move_num = que.popleft()
    que.append(move_num)

print(que[0])

