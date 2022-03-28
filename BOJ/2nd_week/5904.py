# mooo games 

import sys

# moo 수열 생성
# def generating_moo(k):
#     moos = [['m', 'o', 'o'] for _ in range(k+1)]
#     if k < 1:

#         return moos
        
#     else:
#         for i in range(1, k+1):
#             moos[i] = moos[i-1] + ['m', 'o', 'o'] + ['o'] * i + moos[i-1]
#             moos.append(moos[i])
#         return moos[k]
### 이렇게 직접 수열을 생성하게되면 메모리 초과가 날 수밖에 없다. 길이를 통해 해당 수열에 대해 재귀적으로 접근할것. 

# s(k) 수열의 길이 
def L(k):
    if k < 1:
        return 3
    else:
        return L(k-1) + L(k-1) + k + 3

# S(k) = ['m', 'o', 'o', 'm', 'o', 'o', 'o', 'm', 'o', 'o']

# for i in range(N):
#     if L(i) < N <= L(i+1):
#         idx = i + 1
#         break

# length = L(idx)
# => 이렇게 했을때 시간초과가 날 수 밖에 없다. 재귀안에서 계속해서 포문을 부르다 보면 당연히 시간초과가 난다. 

# S(k) 수열의 N 번째 문자를 출력. 이분탐색 사용해야 했으나 그러지 못해서 
# 메모리 초과났음 ㅠ....


##### 종호님의 코드를 그대로 참고하여 이해하는 쪽으로...!! #####################
def minimum_moo_sequence(n, result, k=0):
    # k 는 그냥 0 에서 1씩증가하는 변수로, 함수 선언할때 이렇게 선언해주면 굳이 따로 함수 내부에서 변하는 양을 지정하지 않아도 됨.
    if n <= result:
        return k-1, result
    curr_result = 2 * result + k + 3 
    k, min_len = minimum_moo_sequence(n, curr_result, k+1)
    return k, min_len

def find_location(n):
    k, min_len = minimum_moo_sequence(n, 0)
    prev_len = (min_len - k - 3)//2

    # 2구간의 첫번째 인덱스와 n 이 같다면 m 이다.
    if prev_len + 1 == n:
        return 'm'
    # 이후 인덱스에 n 값이 있다면 무조건 o 이다
    elif prev_len + 1 < n <= min_len - prev_len:
        return 'o'
    # 3구간 에서는 n 에서 (해당 수열의 전체 길이 - 이전 차수 수열의 길이) 를 빼줘서 새로운 n 을 만들어 준다. 
    # 즉 재귀적으로 k-1 로 들어가서 다시 2구간을 살핀다. 이후에 2구간에서 m 혹은 o 라는 return 값을 받으면 차례로 재귀를 탈출한다. 
    else:
        return find_location(n - min_len + prev_len)    


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    print(find_location(n))