s = input()

if s == s.upper():
    print(s.lower())

elif s[0].lower() == s[0] and s[1:].upper() == s[1:]:
    print(s[0].upper() + s[1:].lower())
else:
    print(s)
