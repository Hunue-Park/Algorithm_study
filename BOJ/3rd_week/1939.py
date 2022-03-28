# limitting weight

from collections import deque
import sys
input = sys.stdin.readline

def BFS(mid):
    visited[start] = 1
    # 여기서 q를 선언해 줘야 mid 확인하는 과정에서 
    # 선언되는 BFS 에서 q가 초기화됨. 
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        if now == end:
            return 1
        for nx, nc in graph[now]:
            if visited[nx] == 0 and mid <= nc:
                q.append(nx)
                visited[nx] = 1
    return 0



if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        # for the undirected graph
        graph[a].append([b, c])
        graph[b].append([a, c])
    low, high = 1, 10000000000
    for i in range(1, N+1):
        graph[i].sort(reverse=True)
    start, end = map(int, input().split())
    while low <= high:
        visited = [0 for _ in range(N+1)]
        mid = (low + high) // 2
        if BFS(mid):
            low = mid + 1
        else:
            high = mid - 1
    print(high)
