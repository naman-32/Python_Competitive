n = int(input())
s = input()
#'GRB'
a = 0
for i in range(n - 1):
    if s[i] == s[i + 1]:
        a += 1
        #for j in range(i + 2, n):
        #    if s[i] == s[j]:
        #        a += 1

print(a)
