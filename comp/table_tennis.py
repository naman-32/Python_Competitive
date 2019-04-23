t = int(input())
c = []
for i in range(t):
    x = input()
    c.append(x)

for value in c:
    if value.count('1') > value.count('0'):
        print('WIN')
    else:
        print('LOSE')
