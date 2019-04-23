n = int(input())
X=[]
Y=[]
Z=[]
for i in range(n):
    x,y,z = input().split()
    X.append(int(x))
    Y.append(int(y))
    Z.append(int(z))

if sum(X) == 0 and sum(Y)==0 and sum(Z)==0:
    print('YES')
else:
    print('NO')
