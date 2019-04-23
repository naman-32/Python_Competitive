a, l = [int(n) for n in input().split()]
p = [int(n) for n in input().split()]
p.sort()
m = max(2 * p[0], 2 * (l - p[a - 1]))
for i in range(len(p) - 1):
    if m < p[i + 1] - p[i]:
        m = p[i + 1] - p[i]
print(m / 2)
