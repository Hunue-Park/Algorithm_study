# 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 
# 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 
# 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 
# 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 
# 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

# 출력
# 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.
# def erates(n):
#     if n < 2:
#         return False
    
#     for i in range(2, n):
#         if n % i == 0:
#             return False
    
#     return True

# era_nums = []
# for n in range(1, 10000):
#     if erates(n) == True:
#         era_nums.append(n)
#     else:
#         continue

# T = int(input())
# for _ in range(T):
#     k = int(input())
#     pairs = []
#     for i in range(len(era_nums)):
#         for j in range(1, len(era_nums)):
#             if era_nums[i] + era_nums[j] == k:
#                 a = era_nums[i]
#                 b = era_nums[j]
#                 c = [a, b]
#                 pairs.append(c)
#     ls = len(pairs)
#     point = round(ls / 2)
#     minimun_pair = pairs[point - 1]
#     print(" ".join(map(str, minimun_pair)))


###################### 시간초과 납니다. ###############################

#입력값 이하의 소수 리스트를 만들어 주는 함수.
def prime_list(n):
    #n 개의 True 생성
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        #sieve 의 해당 인덱스가 True 이면 그 인덱스에 해당하는 수는 소수다.
        if sieve[i] == True:
            #i 가 소수였으니 i에 *2 를 한 수부터 n까지 i 간격으로 리스트를 돌며 False 로 바꿔준다. (약수라는 뜻이기 때문.)
            for j in range(i+i, n, i):
                sieve[j] = False
    #최종적으로 for 문을 돌고 나오면 소수가 아닌 수들은 모두 False 처리가 되어있다. (인덱스가 수 의미)
    return [i for i in range(2, n) if sieve[i] == True]

def sosu(n):
    li = prime_list(n)
    idx = max([i for i in range(len(li)) if li[i]<=n/2]) # 여기서 시간초과 컨드롤.
    #i는 줄어들면서 for문을 돌고
    for i in range(idx, -1, -1):
        #j 는 증가하면서 for 문을 돈다.
        for j in range(i, len(li)):
            #그러다가 n 과 일치하는 합을 찾으면 
            if li[i]+li[j]==n:
                #해당 리스트의 값을 돌려준다.
                return [li[i], li[j]]
            
for _ in range(int(input())):
    n = int(input())
    print(" ".join(map(str, sosu(n))))
                



