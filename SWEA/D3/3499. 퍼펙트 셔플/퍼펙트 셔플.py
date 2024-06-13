t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = list(input().split())
    if N % 2 == 0:
        c1 = arr[ : N // 2]
        c2 = arr[N//2 :]
    else:
        c1 = arr[: N // 2 +1]
        c2 = arr[N // 2 + 1:]
    result = []
    while c1 or c2:
        if c1:
            result.append(c1.pop(0))
        if c2:
            result.append(c2.pop(0))

    print(f"#{tc}", *result)