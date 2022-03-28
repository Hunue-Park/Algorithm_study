a = 7
b = 3

c = int(a)
d = int(b)

list = [(c+d), (c-d), (c*d), (c//d), (c%d) ]

print(*list, sep='\n')