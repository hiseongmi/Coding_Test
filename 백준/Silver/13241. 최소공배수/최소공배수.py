import sys
input = sys.stdin.readline
a, b = map(int, input().split())

def gcd(a,b):
    while b:
        a, b = b,  a % b
    return a

print((a * b) // gcd(a,b))