import math
q = input()
a = [int(n) for n in input().split()]
c = 0
for t in range(len(a)):
    s = math.sqrt(a[t]) // 1
    if s * s == a[t] and a[t] != 1:
        for i in range(int(math.sqrt(s)) - 1):
            if (s % (i + 2) == 0):
                print('NO')
                c = 1
                break
        if c == 0:
            print('YES')
        c = 0
    else:
        print("NO")
