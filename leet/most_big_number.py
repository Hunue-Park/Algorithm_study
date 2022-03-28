# 정수를 이어붙여 만들 수 있는 가장 큰수?

# 풀이방법-> 각 숫자 원소의 맨 앞자리 수가 가장 큰 수 여야함. 

numbers = [3, 30, 34, 5, 9]

ans = ""

sorted_nums = list(map(str, numbers))

sorted_nums.sort(key=lambda x: x*3, reverse=True)
# 파이썬만의 강력한 정렬 테크닉!! 

ans = str(int(''.join(sorted_nums)))

print(ans)