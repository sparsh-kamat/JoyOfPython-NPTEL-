L = [int(i) for i in input().split()]
div = []

for i in L:
    if i % 5 == 0 or i % 7 == 0:
        div.append(i)

div.sort()
print(div, end="")
