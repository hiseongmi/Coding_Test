n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
s = 0
A.sort()
for i in range(n):
    b = max(B)
    s += A[i] * b
    B.remove(b)
print(s)