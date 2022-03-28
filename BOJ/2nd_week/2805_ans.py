import sys
input = sys.stdin.readline


def bs(low,high):
    global answer
    if low > high:
        return

    mid = (low+high)//2

    wood = 0
    for tree in trees:
        if tree > mid:
            wood += tree - mid
    #여기서 이렇게만 해도 되는건가? 
    # wood 값이 컸다가 작아지는 경우는? => 한쪽으로만 조건 걸어놓으면 알아서 왔다갔다함. 
    if wood >= m:
        answer = mid
        print(answer, 1)
        bs(mid+1,high)
    else:
        print(mid, 2)
        bs(low,mid-1)
    

n,m = map(int,input().split())
trees = [int(i) for i in input().split()]
answer = 0

bs(0,max(trees))
print(answer)