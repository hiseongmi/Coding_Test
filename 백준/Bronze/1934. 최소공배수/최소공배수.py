import sys
input = sys.stdin.readline
t = int(input().rstrip())
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for tc in range(t):
    a, b = map(int, input().split())
    print((a*b) // gcd(a,b))


