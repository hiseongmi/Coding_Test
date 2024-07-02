t = int(input())
for tc in range(1, t+1):
    a, b = map(int, input().split())
    time = (a+b) % 24
    print(f"#{tc}", time)
    