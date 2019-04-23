count = 0
a = []
n = int(input())
for i in range(n):
    a = [int(i) for i in input().split()]
    if a[1] - a[0] >= 2:
        count = count + 1

print(count)
