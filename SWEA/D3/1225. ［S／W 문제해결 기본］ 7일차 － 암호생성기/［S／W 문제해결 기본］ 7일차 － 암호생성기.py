for tc in range(1, 11):
    t = int(input())
    arr = list(map(int, input().split()))

    while arr[-1] > 0:
        for i in range(1, 6):
            if arr[0] - i > 0:
                arr.append(arr[0] - i)
                arr.pop(0)
            else:
                arr.append(0)
                arr.pop(0)
                break
    print(f"#{t}", *arr)

