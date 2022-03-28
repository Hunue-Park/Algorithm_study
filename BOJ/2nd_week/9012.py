# brakets

import sys

input = sys.stdin.readline

N = int(input())

flag = 0

brakets = [list(input().strip()) for _ in range(N)] 


def judging(bra):
    stack = []
    
    
    for i in range(len(bra)):
        
        if bra[i] == '(':
            stack.append(1)

        elif len(stack) != 0:
            if bra[i] == ')':
                stack.pop()
        elif len(stack) == 0:
            if bra[i] == ')':
                print("NO")
                return
    
    if len(stack) != 0:
        print("NO")
    if len(stack) == 0:
        print("YES")
        
for i in range(N):
    judging(brakets[i])

