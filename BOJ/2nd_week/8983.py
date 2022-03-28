# 사냥꾼. 

import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
# 사대 좌표를 정렬해서 입력받음
shoot_place = sorted(list(map(int, input().split())))
animals = []
for _ in range(N):
    animals.append(list(map(int, input().split())))

# key=lambda axis: axis[0] 설명. 정렬하고자하는 2차원 리스트의 첫번째 값을 기준으로 오름차순 정렬하겠다는 말. 
# 이 문제에서는 동물의 x 좌표가 중요하므로 x 좌표 기준으로 정렬.
animals.sort(key=lambda axis: axis[0])
ans = 0
idx = 0
#동물의 좌표를 기준으로 탐색 시작. (동물 x 좌표 탐색해나간다.)
for i in range(len(animals)):    # O(N*)
    left, right = idx, len(shoot_place) - 1
    mid = 0
    while left <= right:  # O(logM)
        mid = (left + right) // 2
        # 중간인덱스를 가지는 사대의 좌표값이 동물의 x 좌표보다 왼쪽에 있으면
        if shoot_place[mid] <= animals[i][0]:
            # 만약 중간인덱스가 끝값에 도달했거나, 바로 다음 인덱스의 사대좌표가 i번째 동물 x 좌표보다 오른쪽에 있으면
            if len(shoot_place) - 1 == mid or shoot_place[mid+1] > animals[i][0]:
                # while 문의 역할; 동물의 좌표로부터 가장 가까운 사대를 찾는 것을 완료한 것이므로 반복문 탈출. 
                break
            # 못찾았을경우는 시작점을 mid + 1로 해서 이분탐색 계속 진행. 
            left = mid + 1
        # 이외의 경우는 오른쪽에 있다고 할 수 있겠다. 
        else:
            right = mid - 1
    # 이 인덱스는 동물에서 가장 가까운 사대의 좌표를 나타낸다. 
    idx = mid
    # 동물으로부터 가장 가까운 사대와의 거리가 L 이하일때 ans 카운트 1 증가. 
    if abs(animals[i][0] - shoot_place[mid]) + animals[i][1] <= L:
        ans += 1
    # 가장 가까운 사대가 마지막 사대 이고, 동물으로부터 가장 가까운 사대와의 거리가 L 이하일때 ans 카운트 1 증가. 
    elif len(shoot_place) > mid+1 and abs(animals[i][0] - shoot_place[mid+1]) + animals[i][1] <= L:
        ans += 1
## total O(NlogM)
## 동물기준으로 탐색을 진행하기 때문에 중복을 굳이 신경쓰지 않아도 된다. 
print(ans)