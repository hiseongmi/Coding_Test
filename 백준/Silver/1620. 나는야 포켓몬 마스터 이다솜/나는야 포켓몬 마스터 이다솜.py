import sys
input = sys.stdin.readline
n,  m = map(int, input().split())
d = {}
e = {}
for i in range(n):
    p = input().strip() #strip 안하면 /n 이붙음
    d[str(i+1)] = p # 문자출력 d={"1":"asdf"}
    e[p] = i+1 # e={"asdf":"3"}
r = []
for i in range(m):
    q = input().strip() #공백제거
    if q in e:
        r.append(e[q])
    else:
        r.append(d[q])

for i in r:
    print(i)

