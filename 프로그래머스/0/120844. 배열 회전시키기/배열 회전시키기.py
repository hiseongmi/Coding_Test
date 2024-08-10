from collections import deque

def solution(numbers, direction):
    answer = []
    que = deque(numbers)
    if direction == 'right':
        que.rotate(1)
    else:
        que.rotate(-1)
    return list(que)