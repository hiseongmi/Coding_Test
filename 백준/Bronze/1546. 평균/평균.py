import sys
input = sys.stdin.readline

N = int(input())
F = list(map(int, input().split()))
    
max_S = max(F)
for i,  v in enumerate(F):
	F[i] = v/max_S * 100

print(sum(F) / len(F))