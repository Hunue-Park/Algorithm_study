#Hanoi Tower
#no는 출력할때만 원반 번호의미를 띄고
# 재귀함수 호출시에는 옮기는 원반개수의 역할을 한다.

import sys
def move(no, x, y):
    global cnt
    cnt += 1
    
    
    if no > 1 and no <= 20:  
        move(no-1, x, 6-x-y)
           #recur 하향식 분석 참고. 
    moves.append([x, y])
    cnts.append(cnt)
    
    
    #왜 print 가 가운데 있는가? move 함수 자체의 뜻; 
    #원반 번호를 그대로 의마하는 것을 출려하기 위해

    if no > 1 and no <= 20:
        move(no-1, 6-x-y, y)


n = int(sys.stdin.readline())
cnt = 0
cnts = []
moves = []
if n <= 20:
    move(n, 1, 3)
    print(cnts[-1])
    for x, y in moves:
        print(x, y)
    
elif n > 20:
    print(2**n-1)

