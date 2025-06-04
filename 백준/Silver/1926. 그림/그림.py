from collections import deque
n,m = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

def bfs(a, b):
    q = deque([(a,b)])
    cnt = 1
    arr[a][b] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt


paint = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            r = bfs(i, j)
            paint.append(r)

print(len(paint))
print(max(paint) if paint else 0 )