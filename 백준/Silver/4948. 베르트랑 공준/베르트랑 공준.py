import sys
input = sys.stdin.readline

def prime(x):
    if x == 1:
        return False
    for j in range(2, int((x**0.5)+1)):
        if x % j == 0:
            return False
    return True

num = list(range(2,123456*2+1))
r = []
for i in num:
    if prime(i):
        r.append(i)

while True:
    n = int(input().rstrip())
    if n == 0:
        break
    cnt = 0
    for i in r:
        if n< i <=2*n:
            cnt+=1
    print(cnt)