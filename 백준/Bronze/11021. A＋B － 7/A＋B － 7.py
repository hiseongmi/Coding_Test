import sys
input = sys.stdin.readline
t = int(input())
for tc in range(1,t+1):
	A, B = map(int, input().split())
	print(f"Case #{tc}:", A+B)