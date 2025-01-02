def partial(start):
    global ans, cnt
    if sum(ans) == S and len(ans)>0:
        cnt += 1
        
    for i in range(start, N):
        ans.append(arr[i])
        partial(i+1)
        ans.pop()

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
cnt = 0
partial(0)
print(cnt)