# 히스토그램에서 가장 큰 직사각형의 넓이.

import sys

while True:
    # 높이 값 집어넣는 마지막에 0을 넣어서 탐색하다 만나면 종료할 수 있도록
    h = list(map(int, sys.stdin.readline().split())) + [0]
    # 이건 마지막 테스트 케이스 라는 의미
    if h[0] == 0:
        break
    # 이 n 은 히스토그램 막대의 개수. 
    n = h[0]
    stack = [(1, h[1])]
    res = 0
    # n+2 까지 인 이유는 인덱스 상으로는 n+1 까지 갈것이고 n+1 이 0이라서.
    for i in range(2, n+2):
        width = i
        # stack 에 쌓아놨던 마지막 높이값이 i 번째 높입보다 높지 않을때까지 꺼내서 
        # 나의 높이 * 너비 (너비는 현재 인덱스에서 높지않은것 꺼낸 너비를 빼서 구한다.)
        # 여기서 while stack 부분이 stack 리스트를 다 도는 동안으로 한정시켜 준다. 
        while stack and stack[-1][1] > h[i]:
            width, height = stack.pop()
            # 여기서 두개째 꺼내게 되면 너비 인덱스가 2만큼 차이나게 되는것. 
            res = max(res, (i - width) * height)
        # 여기서 스택에 append할때 index가 그대로 너비로 들어가서 
        # 높이가 1이지만 너비가 긴 직사각형의 넓이도 비교 가능. 
        stack.append((width, h[i])) 
    print(res)
