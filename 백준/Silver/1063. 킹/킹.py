k, r, n = input().split()
n = int(n)

moving = [input() for _ in range(n)]

direct = {
    'R':  (0, 1),
    'L':  (0, -1),
    'B':  (1, 0),
    'T':  (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1),
}
alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def pos_al(pos):
    col = alp.index(pos[0])
    row = 8 - int(pos[1])
    return row, col  # 7, 0


king = pos_al(k)
rock = pos_al(r)

for move in moving:
    dx, dy = direct[move]
    nk = (king[0] + dx, king[1] + dy)
    if 0 <= nk[0] < 8 and 0 <= nk[1] < 8:
        if nk == rock:
            nr = (rock[0] + dx, rock[1] + dy)
            if 0 <= nr[0] < 8 and 0 <= nr[1] < 8:
                rock = nr
                king = nk
        else:
            king = nk


def pos_in(pos):
    row = pos[0]
    col = pos[1]
    return alp[col] + str(8 - row)


print(pos_in(king))
print(pos_in(rock))
