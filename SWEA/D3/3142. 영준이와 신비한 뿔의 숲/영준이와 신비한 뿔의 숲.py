t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    ow = 2 * m - n
    tw = m - ow
    print(f"#{tc} {ow} {tw}")
    