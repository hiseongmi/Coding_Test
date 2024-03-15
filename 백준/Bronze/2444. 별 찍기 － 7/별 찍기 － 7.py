N = int(input())


for j in range(1, (2*N)//2+1):
	print(" "*(N-j),end="")
	print("*"*(2*j-1))
for j in range(1,(2*N)//2):
	print(" "*j,end="")
	print("*"*(2*(N-j)-1))