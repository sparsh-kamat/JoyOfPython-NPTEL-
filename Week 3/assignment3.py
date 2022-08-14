L = [int(i) for i in input().split()]
n = 0

for i in L:
    if i % 2 != 0:
        n += 1

print(n, end="")
