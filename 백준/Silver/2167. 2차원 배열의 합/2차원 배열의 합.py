import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
psum = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        psum[i][j] = psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1] + arr[i-1][j-1]
        
K = int(input())
for i in range(K):
    i, j, x, y = map(int, input().split(' '))
    print(psum[x][y] - (psum[x][j-1] + psum[i-1][y]) + psum[i-1][j-1])