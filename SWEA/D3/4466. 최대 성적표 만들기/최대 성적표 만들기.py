t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    print(f"#{tc}", sum(arr[0:k]))