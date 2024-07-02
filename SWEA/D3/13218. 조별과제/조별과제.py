t = int(input())
for tc in range(1, t+1):
    n = int(input())
    team = 0
    if  n <= 2:
        team = 0
    else:
        team = n // 3
    print(f"#{tc}", team)