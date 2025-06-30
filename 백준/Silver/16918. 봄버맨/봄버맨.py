R, C, N = map(int, input().split())
land = [ input() for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bbb(a):
    bomb = [['O'] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if a[i][j] == 'O':
                bomb[i][j] = '.'
            else:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < R and 0 <= ny < C and a[nx][ny] == 'O':
                        bomb[i][j] = '.'
    return bomb


if N <= 1:
    for i in land:
        print(''.join(i))
elif N % 2 == 0:
    for i in range(R):
        print('O'*C)
else:
    t1 = bbb(land)
    t2 = bbb(t1)

    if N % 4 == 3:
        for i in t1:
            print(''.join(i))
    if N % 4 == 1:
        for i in t2:
            print(''.join(i))