#수 정렬하기 3
import sys

N = int(sys.stdin.readline())

blanks = [0] * 10001

for _ in range(N):
    blanks[int(sys.stdin.readline())] += 1

for i in range(10001):
    if blanks[i] != 0:
        for j in range(blanks[i]):
            print(i)


