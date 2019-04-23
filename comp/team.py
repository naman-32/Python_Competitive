n = int(input())
a = 0
for i in range(n):
    x, y, z = map(int, input().split())
    if x + y + z >= 2:
        a += 1


print(a)
