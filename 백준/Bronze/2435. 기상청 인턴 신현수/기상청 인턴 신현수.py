N ,K = map(int,input().split())
arr = list(map(int,input().split()))

current = sum(arr[:K])
result = current

for i in range(N - K):
    current = current - arr[i] + arr[i+K]
    result = max(result,current)

print(result)