s = input()
t = input()
if len(s) == len(t):
    for i in range(len(s)):
        if (s[i] == t[-i - 1]):
            flag = 1
        else:
            flag = 0
            break
else:
    flag = 0
if flag:
    print('YES')
else:
    print('NO')
