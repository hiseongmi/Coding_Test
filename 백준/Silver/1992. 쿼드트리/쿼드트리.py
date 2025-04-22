import sys
input = sys.stdin.readline

n = int(input())
arr = [ list(input()) for _ in range(n)]

result = []
def divide(a,b,n):
    first = arr[a][b]
    for i in range(a, a+n):
        for j in range(b, b+n):
            if arr[i][j] != first:
                result.append('(')
                divide(a,b,n//2)
                divide(a,b+n//2,n//2)
                divide(a+n//2,b,n//2)
                divide(a+n//2,b+n//2,n//2)
                result.append(')')
                return
    result.append(first)
divide(0,0,n)
print(*result,sep='')