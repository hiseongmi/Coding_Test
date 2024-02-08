t = int(input())

for tc in range(1, t+1):
    N=int(input())
    num_list = set(map(int, str(N))) # 중복제거 집합
    x = 2
    while len(num_list) < 10: #0~9가 모두 나올때까지
        new_list = list(map(int, str(N * x)))
        num_list.update(new_list) #update, append 차이 중복제거
        x +=1
    print(f"#{tc}", N*(x - 1))
    