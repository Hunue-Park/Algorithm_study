T = int(input())

for _ in range(T):
    R, lis = input().split()
    r = int(R)
    strs = list(map(str, lis))
    d = len(strs)
    collecs = []
    for i in range(d):
        repeats = strs[i] * r
        collecs.append(repeats)
        
    print(''.join(collecs))