s = input()
l = []
i = 0
while(i <= len(s)):
    l.append(s[i])
    i += 2

l.sort()

j = 0
r = ''
while(j <= len(l)):
   r = (r + l[j] + '+')
   j+=1
#print(r)
print(r[-2::-1])
#print('+'.join(l))
