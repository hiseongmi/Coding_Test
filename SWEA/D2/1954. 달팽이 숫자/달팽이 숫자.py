t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr= [[0]*N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i, j , cnt, dr = 0, 0, 1, 0
    arr[i][j] = cnt
    cnt += 1
    while cnt <= N*N:
        ni = i + di[dr]
        nj = j + dj[dr]
        if 0<= ni < N and 0<= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
            arr[i][j] = cnt
            cnt += 1
        else:
            dr = (dr+1) % 4
            
    print(f"#{tc}")
    for i in range(N):
        print(*arr[i])
    