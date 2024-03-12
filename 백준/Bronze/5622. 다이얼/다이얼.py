alr = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

S=input()
total = 0
for j in range(len(S)):
    for i in alr:
        if S[j] in i:
            total += alr.index(i)+3
print(total)