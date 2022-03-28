function solution(numbers, target) {
    let answer = 0;

    
    function dfs(level, sum) {
        if (level === numbers.length) {
            if (sum === target ) {
                answer += 1;
            }
            return;
        }
        if (check_possible(level, numbers, sum, target)) {
            dfs(level + 1, sum + numbers[level]);
            dfs(level + 1, sum - numbers[level]);        
        }
        function check_possible(idx, numbers, future_value, target) {
            let n = numbers.length;
            for (i = idx; i < n; i++) {
                future_value += numbers[i]
            }
            if (future_value >= target)
                return 1;
            else
                return 0;
        }
        
        
    }
    
    dfs (0, 0);
    
    return answer;
}