N, M = map(int, input().split())
arr =list(map(int, input().split()))
s, e = 1, max(arr) # 1 부터 나무젤높은거
while s <= e:
    H = (s+e) //2  # 중간값부터
    namu = 0
    for i in arr:
        if H < i: #나무가 절단기보다 크면
            namu += (i-H) #잘라서 더하기
    if M <= namu: #가져갈나무보다 크거나 같으면 기존 높이 +1
        s = H +1
    else:
        e = H- 1 # 작으면 기존 높이 -1
        
print(e)