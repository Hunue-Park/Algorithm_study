import sys
import heapq

input=sys.stdin.readline


def main():
    n = int(input())
    points = set()
    lefts = {}
    rights = {}

    for i in range(n):
        L, H, R = map(int, input().split())
        points.add(L)
        points.add(R)
        if not L in lefts:
            lefts[L] = []
        if not R in rights:
            rights[R] = []
        lefts[L].append(H)
        rights[R].append(H)
    # 딕셔너리 형태에서 dictionary[a] 는 a 의 key 값을 가지는 value 를 출력하게 된다. 
    
    # 정렬하기 전에는 set() 으로 감쌌기 때문에 dictionary 형태이다. 
    points = sorted(list(points))
    
    # height 집어넣을 힙. 
    pq_left = [0]
    # pq_left에만 0 이 있는 이유는 밑에서 while 문이 left height 를 기준으로 갱신되기 때문. 
    # 주어진 높이들이 다 빠져도 0 이라는 기본 값이 존재해야한다. 안그러면 heappop할때 에러남. 뺄게없는데 뭘빼 
    pq_right = []
    previous_height = 0
    answers = []
    # points 리스트에는 l,r 좌표 구분없이 들어있다. 
    for point in points:
        if point in lefts:
            for height in lefts[point]:
                # 최대 힙을 만들기 위한 장치. 해당 좌표까지의 높이들이 높이 우선순위로 힙에 들어간다. 
                heapq.heappush(pq_left, -height)
        if point in rights:
            for height in rights[point]:
                heapq.heappush(pq_right, -height)
        while True:
            # right 힙이 비었다면 반복 탈출. 
            if not pq_right:
                break
            # 최대힙이기 때문에 각 트리의 루트가 가장 높은 높이값임. 
            left_top = pq_left[0]
            right_top = pq_right[0]
            # left 와 right 의 최대높이가 다르다면 탈출, 
            if left_top != right_top:
                break
            # 직전 if 문에 안걸리고 넘어왔다는건 left top 과 right top 이 동일한 상태
            heapq.heappop(pq_left)
            heapq.heappop(pq_right)
        left_top = pq_left[0]
        print(left_top)
        # 문제가 원하는 출력값은 높이가 변하는 지점만 관심있으므로 아래 if 문을 통해 해당 좌표 리스트에 저장.
        if previous_height != left_top:
            answers.append([point, -left_top])
            previous_height = left_top
            
    for point, height in answers:
        print(point, height, end = ' ')

if __name__ == '__main__':
    main()