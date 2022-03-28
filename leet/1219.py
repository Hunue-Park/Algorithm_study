# Path with Maximum Gold

# never visit a cell with 0 gold
# you can start and stop collecting gold from any position in the grid
# grid of size M x N 
from collections import deque

grid = [[0,6,0],[5,8,7],[0,9,0]]
M = len(grid)
N = len(grid[0])

def check_range(x, y):
    return 0 <= x < M and 0 <= y < N

def BFS(grid, x, y):
    grid_copy = grid
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append([x,y])
    while q:
        x_pos, y_pos = q.popleft()
        for i in range(4):
            nx = x_pos + dx[i]
            ny = y_pos + dy[i]
            if check_range(nx, ny) and grid[nx][ny] != 0:
                q.append([nx, ny])
        


