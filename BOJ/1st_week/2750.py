#N개의 수가 주어졌을때, 이를 오름차순으로 정렬하는 프로그램을 작성.

N = int(input())

#숫자를 집어넣는 리스트
num_list = []
#N번의 입력을 받는다. 
for _ in range(N):
    s = input()      #여기서 왜 int 를 설정해 줘야하는가? 그냥 문자열로 받게될시 sort를 이용한 정렬에서 1 다음에 2 가 아니라 11 이 오게 될것.
    num_list.append(s)

#오름차순으로 정렬해주는 sorted, 정렬한뒤 
num_list.sort()
# print(num_list)

#N 번 반복해서 리스트의 값들을 출력해준다. 
for k in num_list:
    print(k)