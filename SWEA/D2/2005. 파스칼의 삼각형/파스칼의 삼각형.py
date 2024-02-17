t =int(input())
for tc in range(1,t+1):
    N = int(input())
    p = [[0]*N for _ in range(N)]
    p[0][0] = 1
    for i in range(1,N):
        for j in range(N):
            if j ==0:
                p[i][j] = 1
            else: 
                p[i][j] = p[i-1][j-1]+p[i-1][j]
               
    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            if p[i][j]:
                print(p[i][j], end= " ")
        print()