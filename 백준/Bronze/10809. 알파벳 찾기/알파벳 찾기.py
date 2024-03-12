alr = 'abcdefghijklmnopqrstuvwxyz'
p = []
S = input()
for i in range(len(alr)):
    if alr[i] in S:
        p.append(S.index(alr[i]))
    elif alr[i] not in S:
        p.append(-1)
print(*p)
"""
S = input()
for i in alr:
    if i == S:
        print(S.index(i), end=" ")
    else:
        print(-1, end=" ")
"""