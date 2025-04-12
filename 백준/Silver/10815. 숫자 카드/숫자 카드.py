import sys
input = sys.stdin.readline
n = int(input())
arr = set(map(int, input().split()))
m = int(input())
arr_c = list(map(int, input().split()))
result = []

for i in arr_c:
    if i in arr:
        result.append(1)
    else:
        result.append(0)
print(*result)