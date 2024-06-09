for tc in range(1, 11):
    t = int(input())
    search = input()
    char = input()
    ans = char.count(search)
    print(f"#{tc}", ans)