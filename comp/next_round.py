n, k = map(int, input().split())
lst = []

lst = input().split()

lst = [int(i) for i in lst]
#st = set()
#st = {i for i in lst}
#sat = sorted(st, reverse=True)
#l = sat[k - 1]
a = 0
#print(sat, l)
for i in lst:
    if i > 0 and i >= lst[k - 1]:
        a += 1
print(a)
