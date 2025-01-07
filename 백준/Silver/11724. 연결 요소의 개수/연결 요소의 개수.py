from collections import deque
import sys
input = sys.stdin.readline

def bfs(node, visited, start):
    q = deque([start])
    visited[start] = 1

    while q:
        v = q.popleft()
        for i in node[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                
N, M = map(int,input().split())
node = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0
for _ in range(M):
    u, v = map(int,input().split())
    node[u].append(v)
    node[v].append(u)

for i in range(1, N+1):
    if not visited[i]:
        bfs(node, visited, i)
        cnt += 1
print(cnt)