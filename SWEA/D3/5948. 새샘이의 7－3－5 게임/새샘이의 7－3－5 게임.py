t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    ans = set()
    for i in range(0, len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                ans.add(arr[i]+arr[j]+arr[k])
                
    ans = sorted(list(ans))
    print(f"#{tc}", ans[-5])
    