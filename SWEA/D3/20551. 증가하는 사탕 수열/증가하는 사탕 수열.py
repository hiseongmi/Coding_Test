t = int(input())
for tc in range(1, t + 1):
    a, b, c = map(int, input().split())
    cnt = 0
    while True:
        if a == 0 or b == 0 or c == 0:
            cnt = -1
            break
            
        if b < c:
            if a < b:
                break
            else:
                a -= 1
                cnt += 1
        else:
            b -= 1
            cnt += 1
        
    print(f"#{tc}", cnt)
