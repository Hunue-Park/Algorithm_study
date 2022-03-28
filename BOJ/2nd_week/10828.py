# stack realization 

import sys

input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    commands = list(input().split())
    if commands[0] == 'push':
        stack.append(commands[1])
    if commands[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print('-1')
    if commands[0] == 'size':
        print(len(stack))
    if commands[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if commands[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]

