t = int(input())
for tc in range(1, t+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result = "Possible" #제공 가능
    for i in range(N):
        bread = (arr[i] // M) * K
        if bread < i+1:
            result = "Impossible"
            break
        else:
            result = "Possible"
            
    print(f"#{tc}", result)
