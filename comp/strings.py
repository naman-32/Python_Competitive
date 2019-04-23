s1 = input()
s2 = input()
s1 = s1.lower()
s2 = s2.lower()
t = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(s1)):

    if t.index(s1[i]) > t.index(s2[i]):
        a = 1
        break
    elif t.index(s1[i]) == t.index(s2[i]):
        a = 0
        continue
    else:
        a = -1
        break
print(a)

# s = 'hjdknvjdfhkndfsjkl'
# print(s.find('h'))
