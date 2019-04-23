n = int(input())
l = [4, 7, 47, 44, 74, 77, 447, 444, 474, 477, 774, 777, 744, 747]
a = 0
for i in range(len(l)):
    if (n % l[i]) == 0:
        a = 1
        break
if a == 1:
    print('YES')
else:
    print('NO')
