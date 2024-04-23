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