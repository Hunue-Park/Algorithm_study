# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 
# 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다

import sys

N = int(sys.stdin.readline())

N_nums = sorted(list(map(int, sys.stdin.readline().split())))

M = int(sys.stdin.readline())

M_nums = list(map(int, sys.stdin.readline().split()))


##이분 탐색 ###
#이분 탐색 쓸때는 정렬먼저!!!

def binary_search(array, target, start, end):
    if start > end:
        print(0)
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        print(1)
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    

for i in range(M):
    binary_search(N_nums, M_nums[i], 0, N-1)





    