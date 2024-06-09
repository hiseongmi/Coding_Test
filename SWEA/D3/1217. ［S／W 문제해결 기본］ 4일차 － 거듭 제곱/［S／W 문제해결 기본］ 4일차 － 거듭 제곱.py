def fn(q, s):
    if s == 1:
        return q
    else:
        return q * fn(q, s-1)
   
        
for _ in range(10):
    t = int(input())
    a, b = map(int, input().split())
    ans = fn(a, b)
    
    print(f"#{t}", ans)
