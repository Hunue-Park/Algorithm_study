# 한 심사대에서 동시에 한명만 심사. 
# 더 빨리 끝나는 심사대가 있으면 그곳으로 가서 심사받을 수 있음. 
# 입국심사를 기다리는 사람 수 n
# 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 times
# 모든 사람이 심사를 받는데 걸리는 시간의 최솟값. 

def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        # while 문 돌때마다, 이분탐색의 mid 포인터가 바뀔때마다 people은 초기화
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                print(people)
                break
        if people >= n:
            answer = mid
            right = mid - 1

        elif people < n:
            left = mid + 1
    
    return answer 

if __name__ == "__main__":
    n = 6
    times = [7, 10]
    print(solution(n, times))