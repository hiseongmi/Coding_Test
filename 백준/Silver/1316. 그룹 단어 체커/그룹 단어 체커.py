N = int(input())
count = N

for i in range(N):
	a = str(input())
	for j in range(len(a)-1):
		if a[j] == a[j+1]:
			continue
		elif a[j] in a[j+1:]:
			count -= 1
			break
print(count)