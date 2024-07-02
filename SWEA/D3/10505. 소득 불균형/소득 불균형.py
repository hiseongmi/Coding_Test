t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    avg_arr = sum(arr) / n
    cnt = 0
    for i in arr:
        if avg_arr >= i:
            cnt += 1
    print(f"#{tc}", cnt)