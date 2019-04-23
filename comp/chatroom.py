s = input()
a =0
t = 'hello'
for i in range (len(s)):
    if s[i] == 'h':
        for t in range (i+1,len(s)):
            if s[t] == 'e':
                for u in range (t+1,len(s)):
                    if s[u] == 'l':
                        for v in range (u+1,len(s)):
                            if s[v] == 'l':
                                for w in range (v+1,len(s)):
                                    if s[w] == 'o':
                                        a = 1

                                        break
if a ==1:
    print('YES')
else:
    print('NO')
