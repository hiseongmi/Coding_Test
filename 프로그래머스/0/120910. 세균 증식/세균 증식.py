def solution(n, t):
    answer = n
    for i in range(t):
        answer *=2
    return answer

# return n << t ... 에바지