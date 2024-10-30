def solution(money):
    answer = 0
    
    d1 = [0] * len(money) #[ 0,0,0,0 ]
    d2 = [0] * len(money) #[ 0,0,0,0 ]
    
    d1[1] = max(money[0], money[1]) # [0,1,0,0]
    d1[0] = money[0]
    
    for i in range(2, len(money)-1): #2,3  [0,1,3,2]
        d1[i] = max(d1[i-1], money[i] + d1[i-2])
        
    d2[1] = money[1] #[0,2,0,0]
    for i in range(2, len(money)): #2,3,4  [0,2,3,3]
        d2[i] = max(d2[i-1], money[i] + d2[i-2])
        
    answer = max(max(d1), max(d2))
    
    return answer