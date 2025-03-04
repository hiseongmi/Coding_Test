import sys
input = sys.stdin.readline

n=int(input())
result =[0,9999]
for tc in range(1,n+1):
    j, m = map(int, input().split())
    cnt  = 0
    num = ((j-1) // (1+m))+1
    cnt = 2 * num
    
    if result[1] > cnt:
        result[0] = tc
        result[1] = cnt
        
print(result[0], result[1])
    