n = int(input())
l = [int(n) for n in input().split()]
l.sort(reverse=True)
u = 0
t = 0
a = sum(l)
for i in range(n):
    u += l[i]
    if u * 2 > a:
        break
    else:
        t += 1
print(t + 1)
