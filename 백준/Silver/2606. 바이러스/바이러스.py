from collections import deque

n = int(input())
k = int(input())
cp = [[] for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    cp[a].append(b)
    cp[b].append(a)

def bfs():
    visited = [0] * (n+1)
    visited[1] = 1
    q = deque()
    q.append(1)
    while q:
        c = q.popleft()
        for i in cp[c]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    return sum(visited)


result = bfs() - 1
print(result)