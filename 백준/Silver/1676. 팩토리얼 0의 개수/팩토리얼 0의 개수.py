def zero_c(x):
    cnt = 0
    p = 5
    while x >= p:
        cnt += x // p
        p *= 5
    return cnt 
    
n = int(input())

print(zero_c(n))