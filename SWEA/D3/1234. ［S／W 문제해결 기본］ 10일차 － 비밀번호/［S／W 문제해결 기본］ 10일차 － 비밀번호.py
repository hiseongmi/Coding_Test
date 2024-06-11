for tc in range(1, 11):
    N, arr = input().split()
    pw = []

    for i in arr:
        if not pw or pw[-1] != i:
            pw.append(i)
        else:
            pw.pop()
    if pw[0] == 0:
        pw.pop(pw[0])
    print(f"#{tc}", ''.join(pw))