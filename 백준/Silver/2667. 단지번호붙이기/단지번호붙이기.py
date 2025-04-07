import sys
input = sys.stdin.readline
from collections import deque

n = int(input().strip())
arr = [list(map(int, input().strip())) for _ in range(n)]
cnt = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(r, c):
    que = deque()
    que.append((r, c))
    arr[r][c] = 0
    chk = 1
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    que.append((nx, ny))
                    chk += 1
    return chk


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt.append(bfs(i, j))

print(len(cnt))
cnt.sort()
for i in range(len(cnt)):
    print(cnt[i])
