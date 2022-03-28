#N-queen problem.
#대각선 체크 개념: 행 끼리의 차 == 열기리 차 의 절대값 이면 대각선 상에서 겹치는 것이다. 


import sys

N = int(sys.stdin.readline())


pos = [0] * N #각 열에 배치한 퀸의 위치
# 초기 값은 모두 배치 하지 않았으므로 False로 설정. 배치하면 True. 
flag_a = [False] * N #각 행에 퀸을 배치했는지 체크 
flag_b = [False] * (2 * N - 1) #대각선 방향으로 퀸을 배치 했는지 체크
flag_c = [False] * (2 * N - 1) #반대 대각선 방향으로 퀸을 배치했는지 체크.

def put():
    global count
    for j in range(N):
        for i in range(N):
            print('X' if pos[i] == j else 'O', end='')
        #print()
    #print()
    count += 1
    

def set(i: int):
    
    # 각 행, 대각선 방향에 퀸이 놓아졌는지 체크. not True = False 일때 실행한다. 즉 안놓아졌을때 그 다음 코드를 실행한다.
    for j in range(N):
        if(     not flag_a[j]
            and not flag_b[i+j]
            and not flag_c[i-j + N-1]):
            #j 행 i 열에 배치
            pos[i] = j
            # 모든 열에 배치 했다면 put()함수를 사용해 배치를 출력한다.
            if i == N -1:
                put()
                
            else:
                #i 열 j 행에 배치될때 잡을 수 있는 행과 대각선 방향은 모두 True로 바꾼다. Flag 배열은 놓을 수 있는지 여부를 따지는 곳.
                # 실제 배치는 pos 배열로 부터 온다. 
                flag_a[j] = flag_b[i+j] = flag_c[i - j + N -1 ] = True
                # 다음 열에 퀸을 배치하러 간다. 
                set(i + 1)    # 이과정에서 재귀하고, 다음 열에서 배치할 수 없는 Flag 배열의 True값을 모두 False 로 초기화 한다. 
                # 다음 열에 해당하는 True값은 다시 j 로부터 계산.  
                flag_a[j] = flag_b[i +j] = flag_c[i - j + N -1 ] = False

count = 0
set(0)
print(count)
