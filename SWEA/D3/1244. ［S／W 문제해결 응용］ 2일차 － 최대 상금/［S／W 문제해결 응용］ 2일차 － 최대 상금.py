t = int(input())
for tc in range(1, t+1):
    S, N = input().split()
    N = int(N)
    arr = {S}
    arr_n = set()
    for _ in range(N):
        #횟수만큼 배열 조합 을 arr_n에 넣음 조합이 다 들어갈때까지
        while arr:
            a = arr.pop()
            a = list(a)
            for i in range(len(S)):
                for j in range(i+1, len(S)):
                    a[i], a[j] = a[j], a[i]
                    arr_n.add(''.join(a))
                    a[i], a[j] = a[j], a[i]
        arr, arr_n = arr_n, arr
    print(f"#{tc}", max(map(int, arr)))