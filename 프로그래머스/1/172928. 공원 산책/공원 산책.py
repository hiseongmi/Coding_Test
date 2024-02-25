def solution(park, routes):
    x,y = 0,0
    op = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x, y = i, j
                
    for route in routes:
        w, c = route.split(" ")
        dx, dy = x, y
        for i in range(int(c)):
            nx=x+op[w][0]
            ny=y+op[w][1]
            if 0<=nx<len(park) and 0<=ny<len(park[0]) and park[nx][ny] != "X":
                x, y = nx, ny
            else:
                x, y = dx, dy
                break
    return (x,y)       
