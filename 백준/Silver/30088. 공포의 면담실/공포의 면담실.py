t = int(input())
time = []
for _ in range(t):
    arr = list(map(int,input().split()))
    time.append(sum(arr[1:]))

time.sort()
result = [0] * (t+1)
for i in range(1, t+1):
    result[i] = result[i-1] + time[i-1]

print(sum(result))