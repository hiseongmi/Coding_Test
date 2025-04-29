k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

right = max(arr)
left = 1

while left <= right:
    mid = (left + right) // 2
    total = 0
    for i in range(k):
        total += (arr[i] // mid)
    if total >= n:
        left = mid + 1
    elif total < n:
        right = mid - 1
    else:
        break
print(right)