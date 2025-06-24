import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
answers = []

# 4방향 (상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 십자가 중심에서 시작해 만들 수 있는 최대 크기 찾기
for i in range(n):
    for j in range(m):
        if grid[i][j] != '*':
            continue

        k = 1
        while True:
            valid = True
            for d in range(4):
                nr = i + dr[d] * k
                nc = j + dc[d] * k
                if not (0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '*'):
                    valid = False
                    break
            if not valid:
                break
            k += 1

        max_k = k - 1
        if max_k > 0:
            answers.append((i + 1, j + 1, max_k))  # 1-based index 출력용
            # 방문 표시
            visited[i][j] = True
            for d in range(4):
                for dist in range(1, max_k + 1):
                    nr = i + dr[d] * dist
                    nc = j + dc[d] * dist
                    visited[nr][nc] = True

# 입력에서 *인데 방문 안 된 경우 = 십자가로 커버 안 된 별 → 실패
for i in range(n):
    for j in range(m):
        if grid[i][j] == '*' and not visited[i][j]:
            print(-1)
            sys.exit()

# 출력
print(len(answers))
for a in answers:
    print(*a)
