# 가장 긴 증가하는 수열

N = int(input())

nums = list(map(int, input().split()))

new_nums = sorted(nums)

# find 함수의 역할은 stack에 마지막에 담긴 숫자보다 작거나 같으면 해당숫자를 a 와 교체한다. => 증가하는 수열만 필요하므로!
def find(target):
    start, end = 1, len(stack) - 1
    # 시작점이 끝점보다 작은 동안 반복.
    while start < end:
        # 중간값 계산
        mid = (start + end) // 2
        # stack 리스트의 mid 인덱스의 해당값이 target 보다 작으면
        if stack[mid] < target:
            # 시작점을 중간값 바로 다음 인덱스로 옮김
            start = mid + 1
        # target 보다 크면 
        elif stack[mid] > target:
            # 끝점을 중간값으로 옮김. (왼쪽 영역 탐색하겠다는 의미)
            end = mid
        else:
            # 시작과 끝점을 동일하게 만들고 반복문 탈출 
            start = end = mid
    # end 인덱스를 리턴한다. 
    # 반복문을 탈출할때 결국 end 인덱스를 리턴하니까 해당 인덱스가 있던 곳은 
    # 직전에 다른 값이 있었던 곳이된다. 
    return end

stack = [0]

for a in nums:
    if stack[-1] < a:
        stack.append(a)
        print(stack, 1)
    else:
        stack[find(a)] = a
        print(stack, 2)

#맨 처음 0 하나 길이에서 빼야함
print(len(stack) - 1)


### 결과적으로 이진탐색이 쓰이는 역할은 순서대로 쌓는 stack 리스트를 탐색할때 
### 해당 입력값이 리스트의 제자리를 찾아갈 수 있도록 빠르게 탐색하는 것. 
# 6
# 10 21 10 30 20 50
# [0, 10] 1
# [0, 10, 21] 1
# [0, 10, 21] 2
# [0, 10, 21, 30] 1
# [0, 10, 20, 30] 2
# [0, 10, 20, 30, 50] 1
# 4