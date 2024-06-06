t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    mid = N//2
    arr[mid][mid] = 2
    arr[mid][mid-1] = 1
    arr[mid-1][mid] = 1
    arr[mid-1][mid-1] = 2
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for i in range(M):
        x, y, d = map(int, input().split())

        x, y = x-1, y-1
        arr[x][y] = d
        data = []
        for j in range(8):
            dx, dy = direction[j]
            nx = x + dx
            ny = y + dy
            while True:
                if not (0 <= nx < N and 0 <= ny < N):
                    data = []
                    break
                if arr[nx][ny] == 0:
                    data = []
                    break
                if arr[nx][ny] == d:
                    break
                else:
                    data.append((nx, ny))
                nx, ny = nx + dx, ny + dy
            for tx, ty in data:
                if d == 1:
                    arr[tx][ty] = 1
                elif d == 2:
                    arr[tx][ty] = 2
        w = 0
        b = 0
        for j in range(N):
            w += arr[j].count(2)
            b += arr[j].count(1)

    print(f"#{tc}", b, w)