import sys
input = sys.stdin.readline
n = int(input())
sList = []
for i in range(n):
    s = input()
    sList.append(s)
sList = list(set(sList))
sList.sort(key=lambda x: (len(x),x))
for i in sList:
    print(i, end="")



