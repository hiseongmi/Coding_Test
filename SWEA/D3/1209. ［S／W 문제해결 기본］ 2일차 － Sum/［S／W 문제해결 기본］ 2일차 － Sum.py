for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    r_list = []
    for i in range(100):
        r_s = 0
        for j in range(100):
            r_s += arr[i][j]
        r_list.append(r_s)

    c_list = []
    for i in range(100):
        c_s = 0
        for j in range(100):
            c_s += arr[j][i]
        c_list.append(c_s)

    s1 = 0
    for i in range(100):
        s1 += arr[i][i]
    s2 = 0
    for i in range(100):
        for j in range(100):
            if i + j == 99:
                s2 += arr[i][j]
    f_list = [max(c_list), max(r_list), s1, s2]
    result = max(f_list)
    print(f"#{tc}", result)