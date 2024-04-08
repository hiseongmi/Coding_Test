import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque([i for i in range(1,N+1)])

while len(queue) > 1:
    queue.popleft()
    card = queue.popleft()
    queue.append(card)

print(queue[0])