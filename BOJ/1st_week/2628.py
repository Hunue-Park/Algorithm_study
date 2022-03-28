# 첫줄에는 종이의 가로와 세로의 길이가 차례로 자연수로 주어진다. 가로와 세로의 길이는 최대 100㎝이다. 둘째 줄에는 칼로 잘라야하는 점선의 개수가 주어진다. 
# 셋째 줄부터 마지막 줄까지 한 줄에 점선이 하나씩 아래와 같은 방법으로 입력된다. 가로로 자르는 점선은 0과 점선 번호가 차례로 주어지고, 
# 세로로 자르는 점선은 1과 점선 번호가 주어진다. 입력되는 두 숫자 사이에는 빈 칸이 하나씩 있다.

# 출력
# 첫째 줄에 가장 큰 종이 조각의 넓이를 출력한다. 단, 넓이의 단위는 출력하지 않는다.
x, y = map(int, input().split())
T = int(input())
garo = []
sero = []
for _ in range(T):
    a,b = map(int, input().split())
    if a == 0:
        sero.append(b)
    elif a == 1:
        garo.append(b)
garo.append(0)
garo.append(x)
sero.append(0)
sero.append(y)   
garo.sort()
sero.sort()
garo_dif = []
sero_dif = []
for i in range(len(garo)-1):
    garo_dif.append(garo[i+1]-garo[i])
max_garo = max(garo_dif)
for i in range(len(sero)-1):
    sero_dif.append(sero[i+1]-sero[i])
max_sero = max(sero_dif)

area = max_garo * max_sero

print(area)


    

