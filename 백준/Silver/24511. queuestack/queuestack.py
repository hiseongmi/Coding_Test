from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

que = deque([])
for i in range(N):
    if A[i] == 0:
        que.append(B[i])
for i in range(M):
    que.appendleft(C[i])
    print(que.pop(), end = ' ')