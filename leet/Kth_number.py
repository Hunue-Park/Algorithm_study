# array 의 i 번째 숫자부터 j 번째 숫자까지 자르고 정렬했을때, k번째에 있는 수를 구하려함

from hashlib import new


array = [1, 5, 2, 6, 3, 7, 4]

commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

returns = []
for i in range(len(commands)):
    start_idx = commands[i][0]
    end_idx = commands[i][1]
    target_idx = commands[i][2]

    new_array = array[start_idx - 1 : end_idx]
    new_array.sort()
    returns.append(new_array[target_idx - 1])

print(returns)