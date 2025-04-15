import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
p = sum(arr)
result = 0
for i in arr:
    p -= i
    result += (p*i)
print(result)