import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1 = set(a) - set(b)
b1 = set(b) - set(a)
print(len(a1) + len(b1))