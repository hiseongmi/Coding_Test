import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
total = int(input())
left, right = 0, max(arr)

while left <= right:
    mid = (left + right) // 2
    budget = 0
    for i in arr:
        budget += min(i, mid)
    if budget <= total:
        left = mid + 1
    else:
        right = mid - 1
        
print(right)