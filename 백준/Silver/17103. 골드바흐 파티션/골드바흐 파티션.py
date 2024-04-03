import sys
input = sys.stdin.readline

def prime(x):
    if x == 1:
        return False
    for j in range(2, int((x**0.5)+1)):
        if x % j == 0:
            return False
    return True

num = [1,1] + [0] * 999999
r = []
for i in range(2,1000001):
    if num[i] == 0:
        r.append(i) #초기 소수 넣기
        for j in range(2*i, 1000001, i): # i의 배수 다 제거
            num[j] = 1
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in r:
        if n <= i:
            break
        if not num[n-i] and i <= n-i:
            cnt += 1
    print(cnt)



