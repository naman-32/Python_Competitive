s = input()
s = s.lower()
a = ''
for i in s:
    if not (i == 'a' or i == 'i' or i == 'o' or i == 'e' or i == 'y' or i == 'u'):
        a += ('.' + i)
print(a)
