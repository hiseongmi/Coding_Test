from itertools import permutations

def isprime(i):
    if i < 2:
        return False
    
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True


def solution(numbers):
    answer = []
    number = list(numbers)
    num = []
    for i in range(1, len(numbers)+1):
        num += list(permutations(number, i))
    arr = [int(''.join(t)) for t in num]

    for k in arr:
        if isprime(k):
            answer.append(k)

    return len(set(answer))
