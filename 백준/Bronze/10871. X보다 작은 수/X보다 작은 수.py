import sys
input = sys.stdin.readline
N, X = map(int, input().split())
nums = list(map(int, input().split()))
for i in nums:
	if X > i:
		print(i)