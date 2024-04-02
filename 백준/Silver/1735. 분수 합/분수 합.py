import sys
input = sys.stdin.readline
a, b = list(map(int,input().split()))
a1, b1 = list(map(int,input().split()))
def gcd(a,b):
    while b:
        a, b = b,  a % b
    return a

num = a*b1+b*a1
denom = b*b1

gcd = gcd(num,denom)
num = int(num/gcd)
denom = int(denom/gcd)
print(num, denom)

