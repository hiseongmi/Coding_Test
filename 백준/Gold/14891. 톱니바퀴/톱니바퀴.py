from collections import deque

arr = []
for _ in range(4):
    s = str(input())
    arr.append(deque(i for i in s))


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
    if n > 3:
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


k = int(input())
for i in range(k):
    n, d = map(int, input().split())
    visited = [0 for _ in range(4)]
    direct_turn(n-1,d)
score = 0
if arr[0][0] == "1":
    score+=1
if arr[1][0] == "1":
    score+=2
if arr[2][0] == "1":
    score+=4
if arr[3][0] == "1":
    score+=8
print(score)