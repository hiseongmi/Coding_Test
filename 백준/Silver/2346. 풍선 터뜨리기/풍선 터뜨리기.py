import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
q = deque(enumerate(map(int, input().split())))
arr =[]
while q:
    i, v = q.popleft()
    arr.append(i+1)
    if v > 0:
        q.rotate(-(v-1))
    else:
        q.rotate(-v)
print(' '.join(map(str, arr)))