import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = []
b = []
result=[]
for i in range(n):
	a.append(input().rstrip()) 
for i in range(m):
	b.append(input().rstrip())
    
result= sorted(set(a) & set(b))
print(len(result))
for i in result:
	print(i)