n = int(input())
l = []
al = []
a = 0
for i in range(n):
    l = list(map(int, input().split()))
    a = a - l[0] + l[1]
    al.append(a)
print(max(al))
