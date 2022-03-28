# quick resort! algorithm
import sys

def qsort(nums, left:int, right: int):
    pl = left
    pr = right
    x = nums[(left + right) // 2]

    #교차되기 직전까지만 실행
    while pl <= pr:
        #해당값이 x(피벗값) 보다 작으면 그냥 지나간다 (=> pl += 1)
        while nums[pl] < x:
            pl += 1
        while nums[pr] > x:
            pr -= 1
            #위의 while 문을 통과해서 내려왔다는 것은, nums[pl] >= x or a[pr] <= x 인 경우를 말한다.
            if pl <= pr:  #즉, nums[pl 또는 pr] 값이 피벗값보다 크거나 작은데 pl <= pr 인 경우 
                # 두 인덱스에 해당하는 값을 'swap' 하겠다.
                nums[pl], nums[pr] = nums[pr], nums[pl]
                pl += 1
                pr -= 1  #스왑하고난 다음에는 다시 서로를 향해 간다. 시작 while문이 끝날때까지. 
    #만약 시작 while 문이 끝났는데도 애초 시작점(left) 와 pr(while문 끝날때의 left 그룹의 끝점) 사이에 그룹이 존재한다면
    if left < pr:
        #재귀함수로 qsort 를 불러오는데, 시작점과 끝점이 바뀐 분할된 그룹에서 불러옴.
        qsort(nums, left, pr)
    if pl < right:
        qsort(nums, pl, right)

def quick_sort(nums):
    qsort(nums, 0, n-1)

#################백준 풀기위함 ##########
nums = []
n = int(input())
for _ in range(n):
    nums.append(int(input()))
    print(nums)
    
quick_sort(nums)

for k in nums:
    print(k)

