import sys
input = sys.stdin.readline
n = int(input())
n_card = set(map(int,input().split()))
m = int(input())
m_card = list(map(int,input().split()))
r = []
for i in m_card:
    if i in n_card:
        r.append(1)
    else:
        r.append(0)
print(*r)