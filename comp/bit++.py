n = int(input())
x = 0
for i in range(n):
    s = input()
    if s == '++X' or s == 'X++':
        x += 1
    else:
        x -= 1
print(x)
