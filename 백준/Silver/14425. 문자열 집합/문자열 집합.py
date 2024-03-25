import sys
input = sys.stdin.readline
n, m = map(int, input().split())
S = set([input() for _ in range(n)])
count = 0
for _ in range(m):
    M = input()
    if M in S:
        count += 1

print(count)