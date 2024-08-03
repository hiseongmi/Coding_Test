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
            if 0 <= nx < 16 and 0 <= ny < 16 and v[nx][ny] == 0 and arr[nx][ny] != 1:
                v[nx][ny] = 1
                queue.append((nx, ny))
    return 0


for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    v = [[0] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                x, y = i, j
    ans = bfs(x, y)

    print(f"#{t}", ans)
