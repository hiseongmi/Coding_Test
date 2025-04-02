import sys
input = sys.stdin.readline

n = int(input())
arr = [ tuple(map(int,input().split())) for _ in range(n)]
result = []
for i in arr:
    w, h = i
    rank = 1
    for j in range(n):
        if w < arr[j][0] and h < arr[j][1]:
            rank+=1
    result.append(rank)
print(*result)