n = int(input())
l = []
l = [int(n) for n in input().split()]
x = l.count(1)
y = l.count(2)
z = l.count(3)
m = l.count(4)
a = m
if x >= (2 * y + z):
    if (x - 2 * y - z) % 4 == 0:
        v = 0
    else:
        v = 1
    a = a + y + z + (x - 2 * y - z) // 4 + v
elif x >= z:

    if y >= ((x - z) // 2):
        if ((x - z) % 2) == 0 and (y - ((x - z) // 2)) % 2 == 0:
            d = 0
        else:
            d = 1
        a = a + z + ((x - z) // 2) + (y - ((x - z) // 2)) // 2 + d
    else:
        if (-y + ((x - z) // 2)) % 2 == 0 and (x - z) % 2 == 0:
            e = 0
        else:
            e = 1
        a = a + z + y + (-y + ((x - z) // 2)) // 2 + e
elif x < z:
    # if y >= (z - x) // 2:
    #     if ((z - x) % 2) == 0 and ((y - ((z - x) // 2)) % 2) == 0:
    #         f = 0
    #     else:
    #         f = 1
    #     a = a + z + ((z - x) // 2) + (y - ((z - x) // 2)) // 2 + f
    # else:
    #     if ((z - x) % 2) == 0 and (((z - x) // 2) - y) % 2 == 0:
    #         g = 0
    #     else:
    #         g = 1

    #     a = a + z + y + (((z - x) // 2) - y) // 2 + g
    a = a + z + (y) // 2 + (y) % 2

print(a)
