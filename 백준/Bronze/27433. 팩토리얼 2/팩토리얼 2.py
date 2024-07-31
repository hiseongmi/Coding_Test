def pack(n):
    if n == 1 or n ==0:
        return 1
    else:
        return pack(n-1) * n
    
import sys
input = sys.stdin.readline
N = int(input())
print(pack(N))