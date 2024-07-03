for tc in range(1, 11):
    N = int(input())
    arr = [ list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        flag = 0
        for j in range(N):
            if arr[j][i] == 1:
                flag = 1
            elif arr[j][i] == 2:
                if flag:
                    cnt += 1
                    flag = 0

    print(f"#{tc}", cnt)