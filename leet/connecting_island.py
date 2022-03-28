# n 개의 섬 사이 다리 건설 비용 cost

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    global cnt
    x = find(parent, x)
    y = find(parent, y)
    if x == y:
        return 0
    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]
    return 1

def compare_parent(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x == y:
        return True
    else:
        return False

def solution(n, costs):
    answer = 0
    count = 0
    parent = [0] * n
    rank = [1 for i in range(n+1)]
    for i in range(n):
        parent[i] = i
    costs.sort(key=lambda x: x[2]) # 건설 비용 오름차순 정렬

    
    for x in costs:
        # 섬들을 모두 연결하는데 필요한 다리 개수는 n-1 로 충분. 
        if count == n - 1:
            break
        # x[0] 섬과 x[1] 섬의 부모가 같지 않으면 -> 사이클을 형성하지 않는다면 
        if not compare_parent(parent, x[0], x[1]):
            answer += x[2]
            union(parent, rank, x[0], x[1])
            count += 1
        
    return answer 

costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n = 4

print(solution(4, costs))