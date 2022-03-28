# 괄호열 값 구하기 

import sys

input = sys.stdin.readline


def check_round(brackets):
    stack = []
    for i in brackets:
        if i == "(":
            stack.append(i)

        elif i == "[" or i =="]":
            continue
        else:
            if not stack:       #이전에 ket 을 입력받은 적이 없는 경우 vps 아님.
                #print("NO")
                return 0
            else:
                stack.pop()    #stack에 bra 가 있으므로 꺼냄.
    if not stack:
        #print("YES")  #for 문을 다 돌고 stack이 비었으면 vps.
        return 1
    else:
        #print("NO")   #남은 bra 나 ket이 있다면 vps 아님
        return 0

def check_square(brackets):
    stack = []
    for i in brackets:
        if i == "[":
            stack.append(i)

        elif i == "(" or i ==")":
            continue
        else:
            if not stack:       #이전에 ket 을 입력받은 적이 없는 경우 vps 아님.
                #print("NO")
                return 0
            else:
                stack.pop()    #stack에 bra 가 있으므로 꺼냄.
    if not stack:
        #print("YES")  #for 문을 다 돌고 stack이 비었으면 vps.
        return 1
    else:
        #print("NO")   #남은 bra 나 ket이 있다면 vps 아님
        return 0

brakets = input().strip()
# brakets = (()[[]])([])
bra_lis = list(brakets)

# 계산식 담을 리스트
calculs = []
# 괄호열 자체에 문제가 없으면, 
def calculating(brakets):
    if check_round(brakets) and check_square(brakets):
        for i in range(len(bra_lis) - 1):
            if (
                (bra_lis[i] == "(" and bra_lis[i+1] == "(") or 
                (bra_lis[i] == "(" and bra_lis[i+1] == "[")
            ):
                calculs.append("2 * (")
            elif (
                (bra_lis[i] == "[" and bra_lis[i+1] == "[") or 
                (bra_lis[i] == "[" and bra_lis[i+1] == "(")
            ):
                calculs.append("3 * (")
            elif bra_lis[i] == "(" and bra_lis[i+1] == ")":
                calculs.append("2 ")
            elif bra_lis[i] == "[" and bra_lis[i+1] == "]":
                calculs.append("3 ")
            elif (
                (bra_lis[i] == ")" and bra_lis[i+1] == "(") or 
                (bra_lis[i] == "]" and bra_lis[i+1] == "[") or 
                (bra_lis[i] == ")" and bra_lis[i+1] == "[") or 
                (bra_lis[i] == "]" and bra_lis[i+1] == "(")
            ):
                calculs.append("+ ")
            elif (
                (bra_lis[i] == ")" and bra_lis[i+1] == ")") or
                (bra_lis[i] == "]" and bra_lis[i+1] == "]") or 
                (bra_lis[i] == "]" and bra_lis[i+1] == ")") or
                (bra_lis[i] == ")" and bra_lis[i+1] == "]")
            ):
                calculs.append(") ")
            elif (
                (bra_lis[i] == "(" and bra_lis[i+1] == "]") or
                (bra_lis[i] == "[" and bra_lis[i+1] == ")")
            ):
                print(0)
                return
        # 문자열로 된 리스트의 여러 원소를 하나로 합쳐버리기
        final_calculs = "".join(calculs)

        # 문자열로된 수식을 계산해주는 eval 함수
        print(eval(final_calculs))

    elif not check_square(brakets) or not check_round(brakets):
        print(0)

calculating(brakets)