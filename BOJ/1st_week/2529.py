# 첫 줄에 부등호 문자의 개수를 나타내는 정수 k가 주어진다. 그 다음 줄에는 k개의 부등호 기호가 하나의 공백을 두고 한 줄에 모두 제시된다. 
# k의 범위는 2 ≤ k ≤ 9 이다. 

# 출력
# 여러분은 제시된 부등호 관계를 만족하는 k+1 자리의 최대, 최소 정수를 첫째 줄과 둘째 줄에 각각 출력해야 한다. 
# 단 아래 예(1)과 같이 첫 자리가 0인 경우도 정수에 포함되어야 한다. 
# 모든 입력에 답은 항상 존재하며 출력 정수는 하나의 문자열이 되도록 해야 한다. 
import sys

k = int(sys.stdin.readline())


brakets = list(map(str, sys.stdin.readline().split()))
visited = [0] * 10

max_ans = ""
min_ans = ""

def check(i, j, k):
    #k는 braket 리스트에서 해당 값.
    if k == '<':
        #문자열을 체크만 하고 실제 연산은 따로 적어서 연산.
        return i < j
    else:
        #아래 리턴값들은 True or False 이다. 
        return i > j

def solve(idx, s):
    global max_ans, min_ans

    #여기서 idx 는 brakets리스트의 인덱스,
    # 재귀함수 종료조건. 
    if idx == k+1:
        #min_ans 값에 아무것도 없으면
        if len(min_ans) == 0:
            # s 를 min_ans 에 넣는다. 
            min_ans = s
        else:
            # s 를 max_ans 에 넣는다.
            max_ans = s
        return 
    ###### 여기서부터 재귀함수 호출 시작 #########
    for i in range(10):   #0 ~ 9 까지
        if visited[i] == 0:
            # 맨처음 호출될때는 idx == 0 조건 때문에 넘어가고
            # 그담부터는 check() 함수의 return 값에 따라 넘어간다. 
            # 여기서 미리 유효한 depth 인지 체크해준다. 
            if idx == 0 or check(s[-1], str(i), brakets[idx-1]):
                visited[i] = 1
                #여기서 문자열로 s 에 더하는 이유는 어차피 연산을 하는게 아니라 
                #몇자리 정수 이런식으로 붙여서 쓰기만하면 되기때문.
                solve(idx+1, s+str(i))
                visited[i] = 0
        
solve(0, "")
print(max_ans)
print(min_ans)