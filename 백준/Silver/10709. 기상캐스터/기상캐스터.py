H, W = map(int, input().split())
arr = [input() for _ in range(H)]

for a in arr:
    result = [ -1 for _ in range(W)]
    for i in range(W):
        if a[i] == 'c': # 구름이면 0 넣기 
            result[i] = 0
    tmp = 0
    for i in range(1, W):
        if result[i] == 0: # 새로운 구름 만남 
            tmp = 0
        if result[i-1] != -1 and result[i] != 0:
            tmp+= 1
            result[i] = tmp 
    print(*result)
    