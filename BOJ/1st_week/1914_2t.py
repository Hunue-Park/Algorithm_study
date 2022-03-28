# 하노이 탑 2트 
import sys
N = int(sys.stdin.readline())

def hanoi(n, x, y):
    global cnt
    if n == 0:
        return 
    
    cnt += 1
    
    hanoi(n-1, x, 6-x-y)
    moves.append([x, y])
    cnts.append(cnt)
    hanoi(n-1, 6-x-y, y)
    
    return 
moves = []
cnt = 0
cnts = []

hanoi(N, 1, 3)

print(cnts[-1])
for i in range(len(moves)):
    print(*moves[i])