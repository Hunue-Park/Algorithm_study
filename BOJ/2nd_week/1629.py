# 곱셈
import sys

A, B, C =map(int, sys.stdin.readline().split())


R_s = []
for i in range(C):
    
    R = (A**i) % C
    R_s.append(R)
    if R != 0:
        period = 0
        idx = 0
        for j in range(len(R_s)-1):
            if R_s[j] == R:
                period = len(R_s) - j - 1
                
                break
        if period == 1:
            print(R_s[-1])
            break
        elif period > 1:
            idx = B % period 
            print(R_s[idx])
            break
            
    else:
        print(R, 2)
        break

# 나머지로 나왔던 수가 처음으로 다시 나올때, 나머지의 반복 주기를 계산할 수 있다.
#### 위 알고리즘은 최악의 경우 C 가 소수이고, A,B 가 모두 소수일때 O(N**2) 의 시간복잡도를 가지므로 시간초과. 

# 1000000001 10000000101 999999909
