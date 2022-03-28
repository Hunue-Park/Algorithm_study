# number of islands

class Solution:
    def numIslands(self, grid):
        ans = 0
        q = []
        m = len(grid)
        n = len(grid[0])

        visited = [[0] * n for _ in range(m)]
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for y in range(m):
            for x in range(n):
                if grid[y][x] == "0":
                    continue
                if visited[y][x] == 1:
                    continue
                q.append([y, x])
                visited[y][x] = 1

                ans += 1
                while q:
                    curNode = q.pop()
                    for i in range(4):
                        next_y = curNode[0] + dir[i][0]
                        next_x = curNode[1] + dir[i][1]
                        if next_y >= m or next_x >= n or next_y < 0 or next_x < 0:
                            continue
                        if visited[next_y][next_x] == 1:
                            continue
                        if grid[next_y][next_x] == "0":
                            continue
                        visited[next_y][next_x] = 1
                        q.append([next_y, next_x])
        return ans