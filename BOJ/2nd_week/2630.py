import sys

N = int(sys.stdin.readline())

color_board = []
for _ in range(N):
    color_board.append(list(map(int, sys.stdin.readline().split())))

def Sum_rectangle(x, y, l):
    area = 0
    if l == 1:
        area = color_board[int(x)][int(y)]
        return area
    
    #else:
    for i in range(int(x), int(x+l)):
        for j in range(int(y), int(y+l)):
            area = area + color_board[i][j]
    return area
### 이 함수가 넓이가 1 일때 함수값을 구할수가 없네 

def dfs(N, x, y):
    global white_cnt
    global blue_cnt
    if N < 1:
        return
    if Sum_rectangle(x, y, N) == 0:
        white_cnt += 1
        print(N, "white")
    elif Sum_rectangle(x, y, N) == N**2:
        blue_cnt += 1
        print(N, "blue")
    else:
        
        dfs(int(N/2), x, y) # 1
        dfs(int(N/2), x, y+(N/2))   # 2 
        dfs(int(N/2), x+(N/2), y) # 3
        dfs(int(N/2), x+(N/2), y+(N/2)) # 4 
        

white_cnt = 0
blue_cnt = 0

dfs(N, 0, 0)

print(white_cnt)
print(blue_cnt)