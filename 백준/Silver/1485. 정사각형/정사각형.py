def distance(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2


T = int(input())

for tc in range(T):
    lst = [tuple(map(int, input().split())) for _ in range(4)]
    dists = []

    for i in range(4):
        for j in range(i + 1, 4):
            dists.append(distance(lst[i], lst[j]))
    dists.sort()
    if dists[0] > 0 and dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5] and 2 * dists[0] == dists[4]:
        print(1)
    else:
        print(0)
