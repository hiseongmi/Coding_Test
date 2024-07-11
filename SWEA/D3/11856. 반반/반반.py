t = int(input())
for tc in range(1, t + 1):
    a = input()
    result = ""

    for i in a:
        if a.count(i) == 2:
            result = "Yes"
        else:
            result = "No"
            break
    print(f"#{tc}", result)

