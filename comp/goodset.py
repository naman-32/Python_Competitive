i = 4
goodset = []
while i <= 301:
    goodset.append(str(i))
    i += 3
# print(goodset)

integer = []
t = int(input())
y = 1
while y <= t:
    q = int(input())
    y += 1
    integer.append(q)

for i in integer:
    f = goodset[0:i]
    ans = ' '.join(f)
    print(ans)
#t = int(input())
