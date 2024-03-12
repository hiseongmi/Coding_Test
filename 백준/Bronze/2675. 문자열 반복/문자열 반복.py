for i in range(int(input())):
	a=""
	R, S= map(str,input().split())
	for i in S:
		a += i*int(R)
	print(a)