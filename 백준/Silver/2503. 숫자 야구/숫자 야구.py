from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
n = list(range(1, 10))
allN = list(permutations(n, 3))

for _ in range(N):
    num, S, B = map(int, input().split())
    num = str(num)
    memory = []  # 조건 아닌거 기억하는 곳

    for check_num in allN:
        s, b = 0, 0  # 숫자 조건 체크
        for j in range(3):  # 3자리수니까
            if check_num[j] == int(num[j]):
                s += 1
            elif int(num[j]) in check_num:
                b += 1
        if S != s or B != b:
            memory.append(check_num)  # 조건 아닌거 넣기

    memory_set = set(memory)
    for r in memory:
        allN.remove(r)  # 조건 아닌 값들 지우기

print(len(allN))