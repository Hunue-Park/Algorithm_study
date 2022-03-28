# two liquid
# 문제 설명: 용액들의 특성값이 배열로 주어진다. 용액의 갯수 N 또한 주어진다. 
# 이때 목표는 두개의 용액의 특성값들 중 가장 0에 가까운 두 용액을 찾아내는것. 
# 이분 탐색 사용 할시;
#   예상 스타트 지점 : 특성값의 합 중 가장 작은 값 => 예네를 바꿔야 될듯
#   예상 엔드 지점 : 특성값의 합 중 가장 큰 값. 
#   목표 값: 특성값의 합이 가장 0 에 가까운 경우. => 근데 이걸 정확히 모르는데??? 
#   요 상황에서 매개변수 이분탐색 접근. 

# 투 포인트 예상; 퀵 정렬에서 사용했던 것처럼 왼쪽 끝에서 시작하는 인덱스 체커와 오른쪽 끝에서 시작하는 인덱스 체커 
# 하나씩 진행해 나가는데 각 인덱스의 리스트 값의 합을 계산. 그렇게 계산한 합 중에서 가장 0에 가까운 값을 뽑아냄.

import sys

N = int(sys.stdin.readline())



########## using Two pointer ##########  by 2jinishappy.tistory.com


acid_alkal = sorted(list(map(int, sys.stdin.readline().split())))

# 왼쪽에서 진행하는 포인터
left = 0
# 오른쪽에서부터 진행하는 포인터
right = N - 1
# 출력해야하는 결과값 리스트
ans = [left, right]
# 두 용액 특성값의 합. 합을 구한뒤 절대값을 취해서 대소 비교에 용이하게 만듬. 
m = abs(acid_alkal[left] + acid_alkal[right])
##### => 요 테크닉이 이문제의 가장 핵심. 더한 다음 절대값으로 만들어서 0~ N 사이 값으로 만든다음 최소값 알고리즘 적용.
## => 심지어 이걸로 시작점과 끝점을 정하게 되면, N 의 연산이 필요한 문제에서 N/2 연산이 필요한 문제로 바뀐다. 
##    시간초과를 피하기 위한 방법중 하나로도 사용해볼 수 있다. 


# 포인터 while 문 종료조건; 왼쪽 포인터가 오른쪽보다 왼쪽에 있는 동안만 반복 
while left < right:
    # 두 용액 특성값의 합이 m 보다 작을 경우 m 을 갱신해 나간다. m 의 최소값을 찾는 과정. 
    if abs(acid_alkal[left] + acid_alkal[right]) < m:
        # m을 두 용액 특성값 합의 절대값으로 갱신 
        m = abs(acid_alkal[left] + acid_alkal[right])
        # 출력 리스트는 해당 left 와 right 포인터 인덱스로 저장. 
        ans = [left, right]
    # 왼쪽 포인터가 오른쪽으로 진행하는 과정에서 미리 직후 left 포인터에 의한 특성합을 가져옴 
    left_comp = acid_alkal[left + 1] + acid_alkal[right]
    # 오른쪽 포인터도 동일. 
    right_comp = acid_alkal[left] + acid_alkal[right - 1]
    # 왼쪽 포인터가 진행했을때의 특성합이 오른쪽 포인터가 진행했을때의 특성합보다 작으면;
    # => 더욱 m 값을 최소화 갱신 할 수 있다면. 
    if abs(left_comp) < abs(right_comp):
        # 왼쪽 포인터를 진행시킨다. 
        left += 1
    else:
        right -= 1

# ans리스트의 0번 인덱스는 left 포인터 인덱스 이다. 해당 인덱스를 acid_alkal 리스트에 적용하면 특성값을 출력할 수 있다.
print(str(acid_alkal[ans[0]]) + " "+ str(acid_alkal[ans[1]]))