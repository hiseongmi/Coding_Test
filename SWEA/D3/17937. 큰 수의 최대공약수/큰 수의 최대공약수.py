t = int(input())
for tc in range(1, t+1):
    a, b = map(int, input().split())
    if a == b:
        ans = a
    else:
        ans = 1
    print(f"#{tc}",ans)
