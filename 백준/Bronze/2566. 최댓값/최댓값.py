import sys
input = sys.stdin.readline
nums = []
max_a = 0
max_i = 1
max_j = 1
for _ in range(9):
	a = list(map(int, input().split()))
	nums.append(a)
	if max_a < max(a):
		max_a = max(a)

for i in range(9):
	for j in range(9):
		if nums[i][j] == max_a:
			max_i = i+1
			max_j = j+1

print(max_a)
print(max_i,max_j)