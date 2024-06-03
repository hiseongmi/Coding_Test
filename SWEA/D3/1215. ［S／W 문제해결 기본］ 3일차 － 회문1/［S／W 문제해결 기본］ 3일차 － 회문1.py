for tc in range(1, 11):
    p = int(input())
    arr = [list(input()) for _ in range(8)]
    cnt = 0

    for i in range(8):
        for j in range(8 - p + 1):
            if arr[i][j:j + p] == arr[i][j:j + p][::-1]:
                cnt += 1

    for k in range(8):
        for r in range(8 - p + 1):
            char = ''
            for c in range(r, r + p):
                char += arr[c][k]
            if char == char[::-1]:
                cnt += 1

    print(f"#{tc}", cnt)
