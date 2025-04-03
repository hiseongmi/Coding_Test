import sys
input = sys.stdin.readline

dogam = {}
n, m = map(int, input().split())
for i in range(1, n+1):
    name = input().strip()
    dogam[i] = name
    dogam[name] = i
for j in range(m):
    v = input().strip()
    
    if v.isdigit():
        print(dogam[int(v)])
    else:
        print(dogam[v])
        
    