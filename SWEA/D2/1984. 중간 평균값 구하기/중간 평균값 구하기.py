t = int(input())
for tc in range(1, t+1):
    arr = list(map(int,input().split()))
    arr.sort()
    arr.remove(max(arr))
    arr.remove(min(arr))
    result = sum(arr) / len(arr)
    print(f"#{tc}", round(result))