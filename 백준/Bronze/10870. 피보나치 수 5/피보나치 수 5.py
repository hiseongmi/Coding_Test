def pi(n):
    if n <= 1:
        return n
    return pi(n-1) + pi(n-2)
import sys
input = sys.stdin.readline
N = int(input())
print(pi(N))