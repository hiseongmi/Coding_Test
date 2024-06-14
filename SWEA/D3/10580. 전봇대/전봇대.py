t =int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            a1, b1 = arr[i] # 1 10
            a2, b2 = arr[j] # 5 5
            if (a1 < a2 and b1 > b2) or (a1 > a2 and b1 < b2):
                cnt += 1
    print(f"#{tc}", cnt)