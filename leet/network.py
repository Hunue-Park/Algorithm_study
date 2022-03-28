# network computer. using union find

def solution(n, computers):
    
    answer = 0

    parent = [i for i in range(n)]
    rank = [1 for i in range(n + 1)]

    def find(target):
        if target == parent[target]:
            return target
        parent[target] = find(parent[target])
        return parent[target]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a == b:
            return 0
        if rank[a] > rank[b]:
            parent[b] = a
            rank[a] += rank[b]
        else:
            parent[a] = b
            rank[b] += rank[a]
        return 1
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 0:
                continue
            union(i, j)
    
    for i in range(n):
        parent[i] = find(i)
    
    answer = len(set(parent))

    return answer 