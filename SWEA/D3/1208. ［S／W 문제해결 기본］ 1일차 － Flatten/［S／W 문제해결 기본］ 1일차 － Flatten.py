"""
for tc in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    for i in range(dump):
        a = max(arr)
        arr.remove(a)
        b = min(arr)
        arr.remove(b)
        arr.append(a-1)
        arr.append(b+1)
    ans = max(arr) - min(arr)
    print(f"#{tc}", ans)
"""
for tc in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    for i in range(dump):
        a = max(arr)
        b = min(arr)
        a_i = arr.index(a)
        b_i = arr.index(b)
        arr[a_i] -= 1
        arr[b_i] += 1
    print(f"#{tc}", max(arr) - min(arr))