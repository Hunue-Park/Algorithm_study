def erates(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

T = int(input())

nums = list(map(int, input().split()))
cnt = 0
for i in range(T):
    
    if erates(nums[i]) == True:
        cnt += 1
        
    elif erates(nums[i]) == False:
        cnt = cnt
        

print(cnt)