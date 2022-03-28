# 입력
# 첫째 줄에는 민혁이가 영수에게 몇 번이나 질문을 했는지를 나타내는 1 이상 100 이하의 자연수 N이 주어진다. 
# 이어지는 N개의 줄에는 각 줄마다 민혁이가 질문한 세 자리 수와 영수가 답한 스트라이크 개수를 나타내는 정수와 
# 볼의 개수를 나타내는 정수, 이렇게 총 세 개의 정수가 빈칸을 사이에 두고 주어진다.

# 출력
# 첫 줄에 영수가 생각하고 있을 가능성이 있는 답의 총 개수를 출력한다.
# input 값에 따라 몇번의 연산이 필요할지 대략적으로는 계산해놔야함. 


import sys
from itertools import permutations

N = int(sys.stdin.readline())

TF_table = [0] * 505



clues = []
for _ in range(N):
    inputs = list(map(int, sys.stdin.readline().split()))
    clues.append(inputs)

#clues[i][0] => 민혁이가 던진 숫자
#clues[i][1] => 영수가 답한 스트라이크
#clues[i][2] => 영수가 답한 볼
#clues[i][0] 얘네를 미리미리 각 자리수 분리한 리스트로 바꿔놓으면 코드 리더빌리티가 좀 더 증가할듯.

num = [i for i in range(1, 10)]
whole_nums = list(permutations(num, 3))

def checking(list1, list2):
    stk = 0
    ball = 0
    for i in range(3):
        if list1[i] == list2[i]:
            stk += 1
    for i in range(3):
        for j in range(3):
            if i != j:
                if list1[i] == list2[j]:
                    ball += 1

    return stk, ball
# print(list(whole_nums[1]))
# print(list(map(int, list(str(clues[0][0])))))
# print(checking(whole_nums[1], list(map(int, list(str(clues[0][0]))))))

for i in range(N):
    for j in range(504):
        from_str_to_int_list = list(map(int, list(str(clues[i][0]))))
        if checking(whole_nums[j], from_str_to_int_list) == (clues[i][1], clues[i][2]):
            TF_table[j] += 1

cnt = 0
for i in range(504):
    if TF_table[i] == N:
        cnt += 1
print(cnt)






