분자, 분모 = map(int, input().split())
분자2, 분모2 = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

a1 = (분자*분모2)+(분자2*분모)
a2 = 분모*분모2
gcd = gcd(a1, a2)
a1 = int(a1/gcd)
a2 = int(a2/gcd)

print(a1, a2)