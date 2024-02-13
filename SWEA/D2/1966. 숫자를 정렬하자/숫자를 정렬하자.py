t = int(input())

for tc in range(1, t+1):
    N = int(input())
    num = list(map(int, input().split()))
    r = sorted(num)
    print(f"#{tc}",*r)