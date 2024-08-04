from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    v[x][y] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if arr[nx][ny] == 3:
                return 1
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0 and arr[nx][ny] != 1:
                v[nx][ny] = 1
                queue.append((nx, ny))
    return 0


for tc in range(1, 11):
    t = int(input())
    N = 100
    arr = [list(map(int, input())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j
    ans = bfs(x, y)

    print(f"#{t}", ans)
