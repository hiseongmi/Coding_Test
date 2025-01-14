s = list(map(str,input()))
a = []
b = []
group = s[0]
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        group += s[i]
    else:
        if s[i-1] == '0':
            a.append(group)
        else:
            b.append(group)
        group = s[i]

if group[0] == '0':
    a.append(group)
else:
    b.append(group)
result = min(len(a), len(b))

print(result)