t = int(input())

for tc in range(1, t+1):
    n = int(input())
    result = 0
    for n in range(n+1):
        if n % 2 == 0:
            result -= n
        else: result += n
    print(f'#{tc}',result)
        