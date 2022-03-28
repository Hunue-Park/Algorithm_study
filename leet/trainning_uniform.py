# # 체육복 도난 

# n = 5  # 2<= n <= 30

# lost = [1, 2, 3, 4, 5]

# reserve = [1, 3, 5]

# students = [1] * n

# for i in range(len(lost)):
#     students[lost[i] - 1] -= 1

# for i in range(len(reserve)):
#     students[reserve[i] - 1] += 1
# print(students, "before")
# for i in range(len(students)):
#     if students[i] == 2 and i != len(students) - 1 and students[i + 1] == 0:
#         students[i] -= 1
#         students[i + 1] += 1
#         continue
#     elif students[i] == 2 and students[i - 1] == 0 and i != 0:
#         students[i] -= 1
#         students[i - 1] += 1
#         continue


# # 맨 앞을 맨 끝 바로 뒤에 붙여놓으면 해결될듯.
# cnt = 0
# for i in range(len(students)):
#     if students[i] != 0:
#         cnt += 1
#     else:
#         continue
# print(cnt)
# print(students)

def solution(n, lost, reserve):
    reserve_a = [r for r in reserve if r not in lost]
    lost_a = [a for a in lost if a not in reserve]

    for i in reserve_a:
        left = i - 1
        right = i + 1
        if left in lost_a:
            lost_a.remove(left)
        elif right in lost_a:
            lost_a.remove(right)
    
    return n - len(lost_a)