# n개의 음이아닌 정수. 이 수를 적절히 더하거나 빼서 타겟 넘버 만드는 경우의수 리턴. 
# 주어지는 숫자의 개수는 2개 이상 20개 이하.
# 각 숫자는 1이상 50 이하인 자연수
# 타겟 넘버는 1이상 1000이하인 자연수. 

# how to make? 

def check_possible(idx, numbers, result, target):
    n = len(numbers)
    future_value = result
    for i in range(idx, n):
        future_value += numbers[i]
    if future_value >= target:
        print(f"future value with able: {future_value}")
        return 1
    else:
        print(f"future value with unable: {future_value}")
        return 0


numbers = [1, 1, 1, 1, 1]

target = 3
answer = 0
n = len(numbers)
def dfs(idx, result):
    print(f"idx:{idx}\n result:{result}\n")
    if idx == n:
        if result == target:
            global answer
            answer += 1
        return
    else:
        if check_possible(idx, numbers, result, target):
            dfs(idx+1, result + numbers[idx])
            dfs(idx+1, result - numbers[idx])

dfs(0,0)
print(answer)