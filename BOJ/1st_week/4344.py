# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

def mean(lst):
    value = sum(lst) / len(lst)
    return value

T = int(input())

for _ in range(T):
    nums = list(map(int, input().split()))
    num_of_people = nums[0]
    real_nums = nums[1:]
    avg = mean(real_nums)

    cnt = 0
    k = len(real_nums)
    for i in range(k):
        if real_nums[i] > avg:
            cnt = cnt + 1
        else:
            cnt = cnt
    value = cnt / k
    percent = (round(value, 5)) * 100
    print(f'{percent:.3f}%')





