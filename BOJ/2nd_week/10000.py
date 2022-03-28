# 원 영역. 오일러 지표를 사용한 풀이 feat. UnionFind
# 유니온파인드 구현 
import bisect
import sys
import itertools
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

# 트리를 합치기 전에 랭크를 비교해서 더 짧은 쪽을 더 긴쪽으로 붙인다. 
def union(x, y):
    global cnt
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]
    return 1

N = int(input())
v_list = []
for i in range(N):
    x, r = map(int, input().split())
    v_list.append([x-r, x+r])

# 2차원 리스트를 1차원으로. 
flatten_v = list(itertools.chain.from_iterable(v_list))
comp_v = sorted(list(set(flatten_v)))
L = len(comp_v)
# 2.2.3 초기화 과정. 모든 노드가 자기자신을 부모로 가리킨다.
parent = [0] * L
for i in range(L):
    parent[i] = i
rank = [1 for i in range(L+1)]

for i in range(N):
    # comp_v 에서 v_stack 의 L[i] 좌표보다 이상의 값이 처음으로 나오는 인덱스 - 처음 인덱스
    # 즉 인덱스의 차이를 l 로 선언
    l = bisect.bisect_left(comp_v, v_list[i][0]) 
    r = bisect.bisect_left(comp_v, v_list[i][1])
    union(l, r)
# 아래 for문에서 컴포넌트 수를 세어준다. 
cnt = 0
for i in range(L):
    # 부모가 자기자신인 노드의 갯수는 전체 트리의 개수와 일치한다.
    if i == find(i):
        cnt += 1

e = 2*N
v = L
c = cnt

#오일러 지표 with 2차원 평면 그래프. 
f = c - v + e + 1
print(f)
