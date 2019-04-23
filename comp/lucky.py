n = input()
a = 0
for i in range(len(n)):
    if n[i] == '7' or n[i] == '4':
        a += 1
if a in [4, 7]:
    print('YES')
else:
    print('NO')
