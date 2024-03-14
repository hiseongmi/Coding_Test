import sys
input = sys.stdin.readline
nums = []
for i in range(30):
	nums.append(False)
for i in range(28):
	n = int(input())
	nums[n-1] = True
    
for i in range(30):
	if nums[i] == False:
		print(i+1)