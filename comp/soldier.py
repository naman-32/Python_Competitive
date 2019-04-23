k, n, w = map(int, input().split())
l = k * w * (w + 1) / 2
l = int(l)
if l > n:
    print(l - n)
if l <= n:
    print(0)
