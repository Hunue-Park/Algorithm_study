# 막대기
import sys
input = sys.stdin.readline
N = int(input())

stack = [0]

for _ in range(N):
    num = int(input())
    while stack and stack[-1] <= num:
        stack.pop()
    stack.append(num)
    
    if num < stack[-1]:
        stack.append(num)


print(len(stack))