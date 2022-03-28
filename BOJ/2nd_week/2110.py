# 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 
# 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

# 출력
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

## 공유기의 위치를 어떻게 구현할까? 입력값은 공유기의 개수 밖에 없다. (리스트 쓰지말구)

### 이분 탐색은 찾고자 하는 값이 정렬에 존재하는지 배열을 둘로 쪼개가며 확인하는 방법. 
### 매개변수 탐색은 찾고자 하는 값이 존재하는지 를 확인하지 않고 특정 조건을 만족하는 함수의 결과값에 따라 둘로 쪼개가며 확인. 
## 그렇다면 이 문제의 핵심을 어떤 특정 조건을 만족해야 문제의 해답에 가까워지는지 생각하는 것! 
## 문제의 해답: 가장 인접한 두 공유기 사이의 '최대' 거리.

## "중간값을 기준으로 집의 개수를 셌을 때 C보다 크다면"
import sys
# N, C = map(int, sys.stdin.readline().split())
# home_pos = []
# for _ in range(N):
#     home_pos.append(int(sys.stdin.readline()))

# array_home = sorted(home_pos)

######## android teacher solution #################
N, C = map(int, sys.stdin.readline().split())

home_pos = []
for _ in range(N):
    home_pos.append(int(sys.stdin.readline()))

home_pos.sort()

# 사실 start 와 end 조건을 통해서 굳이 가능한 모든 간격을 따로 리스트에 저장하고 불러오지 않아도 알아서 순회해 준다. 
# 함수에 들어가는 리스트는 특정 좌표값(이 문제에서는 각 집)을 불러오는 용도. 
def binary_search(array, start, end):
    #while 문에서의 이진검색 종료조건
    while start <= end:
        # 이진검색을 위한 중간값 설정. 
        mid = (start + end) // 2
        # 공유기 설치한 집의 좌표를 초기화. 
        installed_house = array[0]
        # 설치한 공유기 갯수 카운팅.
        count = 1
        # 집의 좌표가 나열된 리스트를 순회하며 카운트
        for i in range(1, len(array)):
            #만약 'mid'의 간격으로 공유기를 설치한다고했을때, i 번째 집의 좌표가 처음집 좌표 + 간격 보다 크거나 같으면
            if array[i] >= installed_house + mid:
                # 공유기 설치 카운트를 하나 올리고
                count += 1
                # 공유기를 설치했다는 의미로 installed house 를 array[i] 로 갱신.
                installed_house = array[i]
        # 위의 포문을 돌며 갱신한 카운트(=공유기수)가 목표 공유기 수보다 크거나 같다면, 간격이 현재보다 넓어야 한다는 뜻이므로
        if count >= C:
            global answer    #전역변수 answer
            # 이진탐색 알고리즘에의해 시작지점을 중간값 바로 다음으로 바꾼다. 
            start = mid + 1
            # answer 를 mid 값으로 갱신한다. 
            answer = mid
            print(count, 1)
        else:
            # 카운트 수가 모자라다면 간격의 범위를 왼쪽 절반으로 한정하여 다시 while문을 시작한다. 
            end = mid - 1
            print(count, 2)
            # 여기에서 answer = mid 구문이 없는 이유는 어차피 작아지더라도 다시 커지는 과정에서 해당구문을 
            # 통과할 것이고 답으로 갱신되어 출력될 것이기 때문. 

#################### 최소 간격부터 최대 간격까지 쭉 늘어놓고 그 리스트를 이분탐색 하는 거구나!!!!! #############3

start = 1 # 최소 간격은 1로 넣는 것이 적절하다. 
end = home_pos[-1] - home_pos[0]  # 최대 간격은 가장 멀리 있는 집과 가장 가까이 있는 집의 좌표 차이와 같다. 
answer = 0  # 이진탐색의 중간값이 탐색을 마치면 갱신될 answer 를 선언. 

binary_search(home_pos, start, end)
print(answer)