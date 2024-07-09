t = int(input())
for tc in range(1, t + 1):
    a = input()
    cnt = 0

    cnt += a.count("()")
    cnt += a.count("(|")
    cnt += a.count("|)")
    print(f"#{tc}", cnt)