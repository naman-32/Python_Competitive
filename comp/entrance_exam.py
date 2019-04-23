T = int(input())
while T < 1 or T > 5:
    T = int(input())

for i in range(T):
    N, K, E, M = input().split()
    N = int(N)
    K = int(K)
    E = int(E)
    M = int(M)
    while K < 1 or K >= N or N > 10000 or M < 1 or M > 1000000000 or E < 1 or E > 4:
        N, K, E, M = input().split()
    lg = []
    lst = []
    mine = []
    for i in range(N - 1):
        lg = input().split()
        #    lg.append(x)
        lg = [int(i) for i in lg]
        lst.append(sum(lg))

    lst.sort()
    mine = input().split()
    mine = [int(i) for i in mine]
    t = lst[N - K - 1] + 1 - sum(mine)
    if 0 < t <= M:
        print(t)
    else:
        print('Impossible')
