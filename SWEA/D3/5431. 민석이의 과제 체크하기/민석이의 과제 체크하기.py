t = int(input())
for tc in range(1, t + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    task = [i for i in range(1, N+1)]
    for i in arr:
        task.remove(i)
    
    print(f"#{tc}", *task)
        
