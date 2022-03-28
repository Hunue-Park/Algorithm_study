#일곱난쟁이, 완전탐색.

# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 
# 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.

# 출력
# 일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.
from itertools import combinations
import sys

dwarfs = []
for _ in range(9):
    dwarfs.append(int(sys.stdin.readline().strip()))

combi = list(combinations(dwarfs, 7))


for i in range(len(combi)):
    if sum(combi[i]) == 100:
        ans = list(combi[i])
        break

ans.sort()
for k in ans:
    print(k)


