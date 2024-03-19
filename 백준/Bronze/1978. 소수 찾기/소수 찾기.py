N = int(input())
a = list(map(int, input().split()))
count = 0
for d in a:
    for i in range(2, d+1):
	    if d % i == 0:
		    if d == i:
			    count += 1
		    break
print(count)