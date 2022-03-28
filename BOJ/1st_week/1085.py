# 한수는 지금 (x, y)에 있다. 
# 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.
#입력: 첫째 줄에 x, y, w, h가 주어진다.
# x, y, w, h = map(int, input().split())
x = 3
y = 2
w = 10
h = 3

def compare(crd, length):
    if crd >= length - crd:
        return length - crd
    else:
        return crd



a = compare(x, w)
b = compare(y, h)

if a >= b:
    print(b)
else:
    print(a)

