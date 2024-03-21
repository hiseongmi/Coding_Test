N = int(input())
r = 0
while N >=0:
    if N % 5 ==0:
        r += N // 5
        print(r)
        break
    N-=3
    r+=1
else:
    print(-1)