import sys
input = sys.stdin.readline

num = list(input().split('-'))
arr = []
for i in num:
    n = 0
    for j in i.split('+'):
        n += int(j)
    arr.append(n)
result = arr[0]
for i in range(1, len(arr)):
    result -= arr[i]
print(result)