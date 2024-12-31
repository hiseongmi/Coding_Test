def gop(e_m):
    global ans

    if len(arr) == 2:
        if ans < e_m:
            ans = e_m
            return

    for i in range(1, len(arr)-1):
        e = arr[i-1] * arr[i+1]
        b = arr.pop(i)
        gop(e_m + e)
        arr.insert(i, b)

n = int(input())
arr = list(map(int, input().split()))
ans = 0
gop(0)
print(ans)