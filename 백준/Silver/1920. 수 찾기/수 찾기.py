N = int(input())
N_l = list(map(int, input().split()))
M = int(input())
M_l = list(map(int, input().split()))
N_l.sort()


# m 의 수가 n에 있는지 확인
for i in M_l:
    check = 0
    left = 0
    right = N-1

    while left <= right:
        mid = (left + right) // 2
        if N_l[mid]== i:
            check = 1
            break
        elif N_l[mid] > i:
            right = mid - 1
        else:
            left = mid + 1
    print(check)