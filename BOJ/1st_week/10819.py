# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

# 입력
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

# 출력
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.
import sys
from itertools import permutations
#문제에 해당하는 식을 계산해서 적용하는 함수 생성.
def calcul(nums):
    k = 0
    for i in range(0, len(nums)-1):
        #계산해야하는 식을 하나씩 계산한다음 k값에 갱신.
        k = k + abs(nums[i] - nums[i+1])
    return k 


N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

#A 로만들수있는 모든 '순열'생성. 계산하는 식에서 순서가 중요하기 때문
permutes = list(permutations(A))
#calcul 함수를 이용해 계산한 답을 집어넣는 리스트
cnted_nums = []
for i in range(len(permutes)):
    #permutation 함수로 만들어지는건 튜플이므로 리스트화.
    listed = list(permutes[i])
    converted = calcul(listed)
    cnted_nums.append(converted)
#계산된 값들 중 가장 최대값 출력.
print(max(cnted_nums))





