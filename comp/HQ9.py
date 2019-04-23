s = input()
a = 0
for i in range(len(s)):
    if s[i] == 'H' or s[i] == '9' or s[i] == 'Q':  # or s[i] == '+':
        print('YES')
        a = 1
        break
if a == 0:
    print('NO')
