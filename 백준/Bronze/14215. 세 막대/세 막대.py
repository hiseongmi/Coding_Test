arr = sorted(list(map(int, input().split())))
if arr[2] < arr[1] + arr[0]:
    print(sum(arr))
else:
    print((arr[0]+arr[1])*2 -1)