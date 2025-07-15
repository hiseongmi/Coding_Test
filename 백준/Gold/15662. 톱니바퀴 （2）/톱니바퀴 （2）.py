from collections import deque

def turn(n, d):
    if d == 1:
        arr[n].rotate(1)
    else:
        arr[n].rotate(-1)


def check_left(n, left):
    if n < 0:
        return 0
    if arr[n][2] != left:
        return 1
    return 0


def check_right(n, right):
    if n > (t-1):
        return 0
    if arr[n][6] != right:
        return 1
    return 0


def direct_turn(n, d):
    right = arr[n][2]
    left = arr[n][6]
    turn(n, d)
    visited[n] = 1
    if check_left(n - 1, left) and visited[n - 1] == 0:
        direct_turn(n - 1, -d)
    if check_right(n + 1, right) and visited[n + 1] == 0:
        direct_turn(n + 1, -d)
    return

arr = []
t = int(input())
for _ in range(t):
    s = str(input())
    arr.append(deque(i for i in s))
    
k = int(input())
for i in range(k):
    n, d = map(int, input().split())
    visited = [0 for _ in range(t)]
    direct_turn(n-1, d)

score = 0
for i in range(t):
    if arr[i][0] == "1":
        score += 1
print(score)