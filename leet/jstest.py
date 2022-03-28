def solution(numbers, target):
    answer = 0
    def check_possible(idx, numbers, future_value, target):
        n = len(numbers)
        for i in range(idx, n):
            future_value += numbers[i]
        if future_value >= target:
            return 1
        else:
            return 0
    
        
    n = len(numbers)
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer 
                answer += 1
                return
        else:
            if check_possible(idx, numbers, result, target):
                dfs(idx+1, result + numbers[idx])
                dfs(idx+1, result - numbers[idx])
    dfs(0, 0)
    return answer