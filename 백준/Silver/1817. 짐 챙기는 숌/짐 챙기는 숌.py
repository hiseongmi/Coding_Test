n, m = map(int, input().split())

w = 0
cnt = 1
if n != 0:
    arr = list(map(int, input().split()))
    for i in arr:
        if w + i <= m:
            w += i
        else:
            cnt += 1
            w = i
    print(cnt)
else:
    print(0)

