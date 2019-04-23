h, n = input().split()
h = int(h)
n = int(n)
a = [int(n) for n in input().split()]
t = a[0]
for i in range(n - 1):
    if a[i] <= a[i + 1]:
        t += a[i + 1] - a[i]
    else:
        t += h + a[i + 1] - a[i]

print(t - 1)
