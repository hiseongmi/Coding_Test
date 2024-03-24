import sys
input = sys.stdin.readline
n = int(input())
sort_n = int(''.join(sorted(str(n),reverse=True)))
print(sort_n)