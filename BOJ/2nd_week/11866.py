import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

que = deque([i for i in range(1, N+1)])

orders = []

while que:
    for _ in range(K-1):
        a = que.popleft()
        que.append(a)
    b = que.popleft()
    orders.append(b)
    
print("<", end='')

print(*orders, sep= ', ', end='')

print(">")