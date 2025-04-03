import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dot = list(map(int, input().split()))
dot.sort()


def find_s(d):
    s = 0
    e = n - 1
    while s <= e:
        mid = (s + e) // 2
        if dot[mid] < d:
            s = mid + 1
        else:
            e = mid-1
    return s


def find_e(d):
    s = 0
    e = n - 1
    while s <= e:
        mid = (s + e) // 2
        if dot[mid] > d:
            e = mid - 1
        else:
            s = mid+1
    return e


for i in range(m):
    a, b = map(int, input().split())
    result = find_e(b) - find_s(a) + 1
    print(result)
