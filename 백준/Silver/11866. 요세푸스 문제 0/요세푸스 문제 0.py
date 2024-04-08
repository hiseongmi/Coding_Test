import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
queue = deque([i for i in range(1,N+1)])
print('<', end='')
while True:
    for _ in range(K-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end="")
    if queue:
        print(',', end=" ")
    else:
        break

print('>')
