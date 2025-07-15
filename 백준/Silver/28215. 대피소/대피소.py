from itertools import combinations

n, k = map(int, input().split())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x,y))

def dist(x,y,x2,y2):
    return int(abs(x - x2) + abs(y - y2))


ans = float("INF")
for no in combinations(range(n), k):
    max_d = 0
    for i in range(n):
        x, y = arr[i]
        d = float("INF")
        for j in no:
            x2, y2 = arr[j]
            d = min(d, dist(x, y, x2, y2))
        max_d = max(max_d, d)
    ans = min(ans, max_d)


print(ans)
