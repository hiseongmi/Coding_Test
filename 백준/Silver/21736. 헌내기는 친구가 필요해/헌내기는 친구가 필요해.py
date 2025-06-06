from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]


def bfs(a, b):
    q = deque([(a, b)])
    visited[a][b] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if arr[nx][ny] == 'P':
                    cnt += 1
                    q.append((nx, ny))
                elif arr[nx][ny] == 'O':
                    q.append((nx, ny))

    return cnt


for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            s, e = i, j
result = bfs(s, e)

print(result if result >= 1 else 'TT')
