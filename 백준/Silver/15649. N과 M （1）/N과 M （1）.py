from itertools import permutations

N, M = map(int, input().split())
result =  permutations(range(1, N+1), M)
for ans in result:
    print(*ans)
