# 탑 송수신 관리
# 스택에 집어넣을때 아예 인덱스도 같이 집어넣는게 핵심. 2차원 리스트 형태로. 

import sys
input = sys.stdin.readline

N = int(input())

towers = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []

for i in range(N):
    # stack 에 어느것이라도 들어있다면 반복을 돈다
    while stack:
        # 스택의 마지막 리스트의 높이값이 i 번째 타워높이보다 높다면
        if stack[-1][1] > towers[i]:
            # i 번째 타워높이보다 높은 최초의 타워이므로 해당 인덱스를 answer 리스트에 추가한다. (인덱스이므로 +1)
            answer.append(stack[-1][0] + 1)
            break
        # i 번째 타워높이 보다 높지 않으면 
        else:
            # 높은 값이 나올때까지 pop 한다. 
            stack.pop()
    # 스택이 비어있다면 
    if not stack:
        # stack 을 다돌때까지 i 번째 타워높이보다 높은 타워가 나오지 않았다는 의미이므로 answer 에 0 을 저장. 
        answer.append(0)
    # while 문 브레이크에서 탈출한 후 해당 인덱스의 타워높이를 인덱스값과 함께 stack에 push 한다. 
    # (이후 stack 탐색에서 사용.)
    stack.append([i, towers[i]])
    
print(" ".join(map(str, answer)))