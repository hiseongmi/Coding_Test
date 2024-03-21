N, M = map(int, input().split())
board = [ input() for _ in range(N)]
r = []
for a in range(N-7):
    for b in range(M-7):
        w = 0
        bb = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != "W":
                        w += 1
                    if board[i][j] != "B":
                        bb += 1
                else:
                    if board[i][j] != "B":
                        w += 1
                    if board[i][j] != "W":
                        bb += 1
        r.append(w)
        r.append(bb)
print(min(r))
