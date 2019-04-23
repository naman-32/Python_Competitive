n, m, a = map(int, input().split())

if n % a != 0:
    A = n // a + 1
else:
    A = n / a
if m % a != 0:
    B = m // a + 1
else:
    B = m / a
print(A * B)
