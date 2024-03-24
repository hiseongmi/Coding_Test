import sys
input = sys.stdin.readline
n = int(input())
m = list(map(int,input().split()))
m_set = sorted(list(set(m)))
m_dict = {key: value for value, key in enumerate(m_set)}

for v in m:
    print(m_dict[v], end=" ")
