k, t = input().split()
k = int(k)
t = int(t)
s = input()
flag = 1
for j in range(t):
    for i in range(len(s) - 1):
        if s[i] == 'B' and s[i + 1] == 'G' and flag:
            s = s[:i] + 'G' + 'B' + s[i + 2:]
            flag = 0
        else:
            flag = 1
    flag = 1
print(s)
