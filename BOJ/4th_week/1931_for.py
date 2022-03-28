import sys

input = sys.stdin.readline

n = int(input())
time = []
for i in range(n):
    first, second = map(int, input().split())
    time.append([first, second])
time.sort(key=lambda x: (x[1], x[0]))

last = 0
cnt = 0
for i,j in time:
    if i >= last:
        cnt += 1
        last = j

print(cnt)