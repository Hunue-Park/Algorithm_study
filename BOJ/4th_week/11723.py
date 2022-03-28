# set. with bitmasking

import sys
from types import MemberDescriptorType
input = sys.stdin.readline

N = int(input())

S = 0b0

# # bitmasking adding element

# n = 3
# bin(0b0010 | (1 << n))

# # delete element

# bin(0b1010 & ~(1 << n))

# # checking n_th element

# bin(0b1010 & (1 << n))

# # toggle

# bin(0b1010 ^ (1 << n))

for i in range(N):
    cmds, *n = input().split()
    if cmds == 'add':
        S = S | (1 << int(n[0]) - 1)
        continue
    elif cmds == 'check':
        if S & (1 << int(n[0]) - 1) != 0:
            print(1)
        else:
            print(0)
    elif cmds == 'remove':
        S = S & ~(1 << int(n[0]) - 1)
    elif cmds == 'toggle':
        S = S ^ (1 << int(n[0]) - 1)
    elif cmds == 'all':
        S = 0b11111111111111111111
    elif cmds == 'empty':
        S = 0b00000000000000000000
    