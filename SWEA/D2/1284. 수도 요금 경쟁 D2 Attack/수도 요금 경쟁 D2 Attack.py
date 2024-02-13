t = int(input())

for tc in range(1, t+1):
    P, Q, R, S, W = map(int, input().split())
    
    A = W * P # 한달 요금
    
    if W < R:
        B = Q
    else: 
        O = W - R
        B = Q + (O * S)
        
   
    print(f"#{tc}",B) if int(A) >int(B) else print(f"#{tc}",A)