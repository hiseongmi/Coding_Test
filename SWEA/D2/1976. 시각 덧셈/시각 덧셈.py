t = int(input())
for tc in range(1, t+1):
    a, a1, b, b1 = map(int, input().split())
    s = a + b
    m = a1 + b1
    if s > 12:
        s -= 12
    if m > 59:
        m -= 60
        s += 1
    print(f"#{tc}", s, m)
