import sys
input = sys.stdin.readline

n = int(input())
count =[0] * 10001

for i in range(n):
    arr = int(input())
    count[arr] += 1
    
for i in range(len(count)):
    for _ in range(count[i]):
        print(i)