a,b = [int(input()) for _ in  range(2)]

c = b // 100
d = b // 10 - 10*c
e = b - 100*c - 10*d
f = a * b
nums = [e, d, c]

for i in range (3):
    print(a * nums[i])
print(f)