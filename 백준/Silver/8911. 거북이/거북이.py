import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a = input()
    #0 : 북, 1: 남, 2: 서, 3: 동
    dr = (-1, 1, 0, 0)  # 행
    dc = (0,0,-1,1) # 열
    dL = (2, 3, 1, 0) # 왼쪽 회전 
    dR = (3, 2, 0, 1) # 오른쪽 회전
    
    min_r, min_c, max_r, max_c = 0,0,0,0
    r, c, d = 0,0,0
    
    for move in a:
        if move == "L":
            d = dL[d]
            continue
        elif move == "R":
            d = dR[d]
            continue
        elif move == "F":
            r += dr[d]
            c += dc[d]
        elif move == "B":
            r -= dr[d]
            c -= dc[d]
            
        min_r = min(min_r, r)
        max_r = max(max_r, r)
        min_c = min(min_c, c)
        max_c = max(max_c, c)
        
    print(abs(max_r - min_r) * abs(max_c - min_c))
    