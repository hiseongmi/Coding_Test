t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(input().split()) for _ in range(n) ]
    money = 0
    for p, x in arr:
        money += float(p) * int(x)
    print(f"#{tc}", money)