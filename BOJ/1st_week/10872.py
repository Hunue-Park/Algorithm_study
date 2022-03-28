# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

N = int(input())

if N == 0:
    
    print(1)
else:
    ans = 1
    for i in range(1,N+1):
        ans = ans * i

    print(ans)