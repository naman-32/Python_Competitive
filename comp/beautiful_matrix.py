l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
l3 = [int(x) for x in input().split()]
l4 = [int(x) for x in input().split()]
l5 = [int(x) for x in input().split()]
if 1 in l1:
    x = l1.index(1) + 1
    y = 1
if 1 in l2:
    x = l2.index(1) + 1
    y = 2
if 1 in l3:
    x = l3.index(1) + 1
    y = 3
if 1 in l4:
    x = l4.index(1) + 1
    y = 4
if 1 in l5:
    x = l5.index(1) + 1
    y = 5
d = abs(x - 3)
f = abs(y - 3)
print(d + f)
