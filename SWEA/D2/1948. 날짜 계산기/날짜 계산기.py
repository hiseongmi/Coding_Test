t = int(input())
for tc in range(1, t+1):
    m1, d1, m2, d2 = map(int, input().split())
    month = {1:31, 2:28, 3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30, 12:31}
    result = 0
    if m1 == m2:
        result = d2 - d1 + 1 
    else: 
        for i in range(m1, m2+1):
            if i == m1:
                result += month[i] - d1 +1
            elif i == m2:
                result += d2
            else: result += month[i]
    print(f"#{tc}", result)