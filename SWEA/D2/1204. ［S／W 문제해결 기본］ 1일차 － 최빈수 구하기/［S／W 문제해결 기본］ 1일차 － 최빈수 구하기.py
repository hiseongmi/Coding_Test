
T = int(input())
for tc in range(1, T+1):
    tc =input()
    arr = list(map(int, input().split()))
    cnt  =[0] * 101
    m = 0
    for i in arr:
        cnt[i] += 1
        if cnt[i] >= cnt[m]: 
            m = i
    print(f"#{tc}", m)