t = int(input())

for tc in range(1,t+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if N > M:
        N, M = M, N
        A, B = B, A
    
    result = 0
    for i in range(M-N+1):
        t = 0
        for j in range(N):
            t += A[j] * B[j+i]
            
        if t > result:
            result = t
                
    print(f"#{tc}", result)