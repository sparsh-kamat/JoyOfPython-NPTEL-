n = input()
L = [int(i) for i in input().split()]

L.sort(reverse=True)
subset = L[:int(n)]

print(subset, end="")
