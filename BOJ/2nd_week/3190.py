# snake game 
# 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

# 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다
# -> 인덱스 주의; [0][0] 아님
# first, make simple simulation. 

import sys
from collections import deque

input = sys.stdin.readline

def change(d, c):
    # up 0 right 1 down 2 left 3
    if c == "L":
        d = (d - 1) % 4
        # 와... 이거 어차피 음수 나와도 리스트 인덱스라 -1 = 3 이다. 
    else:
        d = (d + 1) % 4
    return d

# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def start():
    # 초기 방향
    direction = 1
    # 시간 
    time = 1
    # 초기 뱀 위치
    y, x = 0, 0
    # 방문 위치
    visited = deque([[y, x]])
    # arr 가 뱀이 움직이는 보드. 뱀이 있다 => 2, 사과가 있다 => 1 지나갔다 => 0
    arr[y][x] = 2
    while True:
        y, x = y + dy[direction], x + dx[direction]
        # 즉 arr[y][x] != 2 라는 조건은 움직이려고 하는 y,x 에 자신이 있냐 없냐를 확인해줌. 
        if 0 <= y < N and 0 <= x < N and arr[y][x] != 2:
            # 사과가 없는 경우
            if not arr[y][x] == 1:
                temp_y, temp_x = visited.popleft()
                # 꼬리 제거
                arr[temp_y][temp_x] = 0
            arr[y][x] = 2
            # 방문했다는 의미로 visited que에 append 한다. 
            visited.append([y, x])
            if time in times.keys():
                # times 의 time 에는 해당 시간에 전환해야할 방향정보가 들어있다. 
                direction = change(direction, times[time])
            # while 문안에서 if 한번 돌때마다 time += 1, time 이 마치 count 역할. 
            time += 1
        # 자기 몸에 부딪히거나, 벽에 부딪힌경우
        else:
            return time

if __name__ == "__main__":
    N = int(input())
    K = int(input())
    arr = [[0] * N for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        # 사과 좌표 저장. 
        arr[a-1][b-1] = 1
    L = int(input())
    times = {}
    for i in range(L):
        X, C = input().split()
        times[int(X)] = C
    
    print(arr)

    print(start())
