import sys
input = sys.stdin.readline
N, M =map(int, input().split())
b = [0] * N
for z in range(M):
	i , j , k = map(int, input().split())
	for x in range(i, j+1):
		b[x-1] = k
		
print(*b)