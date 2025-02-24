import sys
input = sys.stdin.readline

N = int(input())
paper = [ list(map(int, input().split())) for _ in range(N) ]
answer = [0] * 3

def solution(x,y,N):
    global answer
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                for a in range(3):
                    for b in range(3):
                        solution(x+(N//3)*a,y+(N//3)*b, N//3)
                return
    if color == -1:
        answer[0] += 1
    elif color == 0:
        answer[1] += 1
    else:
        answer[2] += 1
solution(0,0,N)
print(answer[0])
print(answer[1])
print(answer[2])