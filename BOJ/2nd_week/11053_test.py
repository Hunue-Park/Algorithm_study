# the longest increasing numbers
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

new_nums = sorted(nums)

def find(target):
    start, end = 1, len(stack) - 1
    while start < end:
        mid = (start + end) // 2
        if stack[mid] < target:
            start = mid + 1
        elif stack[mid] > target:
            end = mid
        else:
            start = end = mid
    return end

stack = [0]
# 단 스택을 쓰려면 정렬된 숫자 리스트여야 가능함. 안그러면 흠... 최대힙 에서 차례차례 뺴오기 정도? 
for a in nums:
    if stack[-1] < a:
        stack.append(a)
    # a 의 크기에 해당하는 인덱스를 찾아서 a 로 교체해줌. find 가 반환하는것은 결국 stack 의 인덱스 이기때문에.
    else:
        stack[find(a)] = a

print(len(stack) - 1)