s = input()
a = 2
for i in range(len(s) - 6):
    for j in range(i, i + 7):
        if s[j] == '0':
            a = 0
        else:
            a = 2
            break
    for j in range(i, i + 7):
        if s[j] == '1':
            a = 1
        else:
            if a != 0:
                a = 2
            break
    if a == 1 or a == 0:
        break
if (a == 1 or a == 0) and len(s) >= 7:
    print('YES')
else:
    print('NO')
