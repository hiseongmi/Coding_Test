t =int(input())
for tc in range(1, t+1):
    L, U, X = map(int, input().split())
    ans = 0
    if U <= X:
        ans = -1
    elif X <= L:
        ans = L - X

    print(f"#{tc}", ans)