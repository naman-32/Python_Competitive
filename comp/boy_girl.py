s = input()
r = []
for i in range(len(s)):
    r.append(s[i])
t = set()
t = {n for n in r}
if len(t) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
