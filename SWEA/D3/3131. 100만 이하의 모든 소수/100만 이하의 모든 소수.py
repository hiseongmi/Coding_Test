def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


arr = []
for i in range(2, int(10**6)):
    if prime(i):
        arr.append(i)
print(*arr)
