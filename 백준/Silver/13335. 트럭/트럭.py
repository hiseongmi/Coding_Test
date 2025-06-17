from collections import deque 

n, w, L = map(int, input().split(" "))
B = deque(list(map(int, input().split())))
que = deque([0] * w)
time = 0
while que:
    time += 1
    que.popleft()
    if B:
        if sum(que) + B[0] <= L:
            que.append(B.popleft())
        else:
            que.append(0) # 0을 넣어서 길이 w를 유지하게 함
print(time)