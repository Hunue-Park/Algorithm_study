# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 
# 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
# 나머지 연산 : %
def checking_4(num1):
    if num1 % 4 == 0:
        return 30
    if num1 % 4 != 0:
        return 40


def checking_100(num1):
    if num1 % 100 == 0:
        return 0
    if num1 % 100 != 0:
        return 1

def checking_400(num1):
    if num1 % 400 == 0:
        return -1
    if num1 % 400 != 0:
        return 10


input_value = 2000
c = checking_4(input_value) + checking_100(input_value) + checking_400(input_value)

if c == 29:
    print(1)
elif c == 41:
    print(1)
else: 
    print(0)


