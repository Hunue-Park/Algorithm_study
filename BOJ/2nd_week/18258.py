# que 2

import sys
from collections import deque

n = int(sys.stdin.readline())
# 빈 큐 만들기
que = deque()

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        que.append(command[-1])
    # pop 명령어일때
    elif command[0] == 'pop':
        # 큐 가 비어있다면 -1 출력
        if not que:
            print(-1)
        # 큐에 값이 들어있다면 popleft 내장 함수 사용해서 que 의 pop을 구현
        else:
            print(que.popleft())
    elif command[0] == 'size':
        print(len(que))
    elif command[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])
    elif command[0] == 'back':
        if not que:
            print(-1)
        else:
            print(que[-1])