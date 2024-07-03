t = int(input())
for tc in range(1, t+1):
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b+1):
        n = i ** 0.5
        if n == int(n):
            n = str(int(n))
            i = str(i)
            if i == i[::-1] and n == n[::-1]:
                cnt += 1
    print(f"#{tc}", cnt)