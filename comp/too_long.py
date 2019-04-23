n = int(input())
lst = []
for i in range(n):
    s = input()
    if len(s) > 10:
        t = s[0] + str(len(s) - 2) + s[-1]
        lst.append(t)
    else:
        print(s)
for i in lst:
    print(i)

print(lst)
