s = input()
a = 0
for i in range(len(s) - 6):
    if ((s[i:i + 7] == '0000000') or (s[i:i + 7] == '1111111')):
        print('YES')
        a = 1
        break


if a == 0 or len(s) < 7:
    print('NO')
# if ((i == (len(s) - 7)) or (len(s) <= 7)):
  #   print('NO')
